#include <chrono>
#include <iostream>
#include <unordered_set>
#include <set>
#include <string>
#include <sstream>
#include <functional>



template<typename Set>
void reserve(Set &s, std::size_t cnt, float load_factor){
}

typedef std::unordered_set<size_t> uSet;
template<>
void reserve(uSet &s, std::size_t cnt, float load_factor){
    s.max_load_factor(load_factor);
    s.reserve(cnt);
}



template<typename Set>
void put_out_statistics(Set &s){
}

template<>
void put_out_statistics(uSet &s){
  size_t  b_cnt=s.bucket_count();
  std::cout<<"bucked_cnt: "<<b_cnt<<"\n";
  size_t max_per_bucket=0;
  for(size_t i=0;i<b_cnt;i++){
    max_per_bucket=std::max(max_per_bucket, s.bucket_size(i));
  }
  std::cout<<"load_factor "<<s.load_factor()<<"\n";
  std::cout<<"max_per_bucket "<<max_per_bucket<<"\n";
}




template<typename Set>
std::string header(float load_factor){
}


template<>
std::string header<uSet>(float load_factor){

   std::stringstream ss;
   ss<<"c++ unordered_set ( max_load_factor="<<load_factor<<")";
   return ss.str();
}


typedef std::set<size_t> tSet;
template<>
std::string header<tSet>(float load_factor){
   return "c++ std::set";
}

size_t operation_test(const std::function <void (void)>& f, size_t n, const std::string &label)
{  
   auto begin = std::chrono::high_resolution_clock::now();
   f();
   auto end = std::chrono::high_resolution_clock::now();
   std::cout << n <<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(n*1e9)
             << " sec per " <<label<< std::endl;
}


template <typename Set>
size_t do_test(size_t size, float load_factor){
   size_t sum=0;
   
   std::cout<<"\n\n########## testisting "<<header<Set>(load_factor)<<":\n";
    
   Set set;
   reserve(set, size, load_factor);


   //insert
   operation_test([&set, size](){
      for(size_t i=0;i<size;i++)
     set.insert(i);
   }, size, "add");
   
   
   //iterating through
   operation_test([&set, &sum, size](){
      for(typename Set::const_iterator it=set.begin(); it!=set.end(); ++it)
       sum+=*it;
   }, size, "iterating through");

   
   //nonexisting look_up
   operation_test([&set, &sum, size](){
      for(size_t i=size;i<size*2;i++)
       sum+=set.count(i);
   }, size, "nonexisting lookup");

   
   //existing look_up
   operation_test([&set, &sum, size](){
      for(size_t i=0;i<size;i++)
       sum+=set.count(i);
   }, size, "existing lookup");
   
   sum-=set.size();
   put_out_statistics(set);
   
   //nonexisting delete:
   operation_test([&set, size](){
      for(size_t i=size;i<size*2;i++)
        set.erase(i);
   }, size, "discarding nonexisting");

     
   //delete existing
   operation_test([&set, size](){
      for(size_t i=0;i<size;i++)
        set.erase(i);
   }, size, "discarding existing");
   
   
   std::cout<<"\n########## testisting  done for "<<header<Set>(load_factor)<<":\n\n";
    
   return set.size();

}
