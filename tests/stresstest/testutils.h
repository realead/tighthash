#include <chrono>
#include <iostream>
#include <unordered_set>
#include <set>
#include <string>
#include <sstream>



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



template <typename Set>
size_t do_test(size_t size, float load_factor){
   size_t sum=0;
   
   std::cout<<"\n\n########## testisting "<<header<Set>(load_factor)<<":\n";
    
   Set set;
   reserve(set, size, load_factor);

   //insert
   auto begin = std::chrono::high_resolution_clock::now();
   for(size_t i=0;i<size;i++)
     set.insert(i);
   auto end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per add" << std::endl;
   
   
   //iterating through
   begin = std::chrono::high_resolution_clock::now();
    
   for(typename Set::const_iterator it=set.begin(); it!=set.end(); ++it)
       sum+=*it;
    
   end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per iterating through" << std::endl;
   
   //nonexisting look_up
   begin = std::chrono::high_resolution_clock::now();
    
   for(size_t i=size;i<size*2;i++)
       sum+=set.count(i);
    
   end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per nonexisting lookup" << std::endl;
   
   
   //existing look_up
   begin = std::chrono::high_resolution_clock::now();
    
   for(size_t i=0;i<size;i++)
       sum+=set.count(i);
    
   end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per existing lookup" << std::endl;
   
   sum-=set.size();
   put_out_statistics(set);
   
   //nonexisting delete:
   begin = std::chrono::high_resolution_clock::now();
   for(size_t i=size;i<size*2;i++)
      set.erase(i);
   end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per discarding nonexisting " << std::endl;
     

   //delete existing
   begin = std::chrono::high_resolution_clock::now();
   for(size_t i=0;i<size;i++)
      set.erase(i);
   end = std::chrono::high_resolution_clock::now();
   std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per discarding existing " << std::endl;
   
   
   std::cout<<"\n########## testisting  done for "<<header<Set>(load_factor)<<":\n\n";
    
   return sum+set.size();

}
