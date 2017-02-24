#include <chrono>
#include <iostream>

template <typename Set>
size_t do_test(){
    std::size_t sizes[4]={10000, 100000, 1000000, 10000000};
    
    size_t sum=0;
    for(auto size : sizes){
       Set set;

       auto begin = std::chrono::high_resolution_clock::now();
       for(size_t i=0;i<size;i++)
         set.insert(i);
       auto end = std::chrono::high_resolution_clock::now();
       std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per add" << std::endl;
        
       begin = std::chrono::high_resolution_clock::now();
        
       for(size_t i=0;i<size;i++)
        sum+=set.count(i);
       end = std::chrono::high_resolution_clock::now();
       std::cout <<size<<": "<<std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()/(size*1e9)<< " sec per lookup" << std::endl;
      
    }
    
    return sum;

}
