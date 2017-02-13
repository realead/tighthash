from cpython cimport array
import array
import random
import math


_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]


cdef class TightHashSet:
    cdef unsigned long long int __cnt
    cdef double min_factor
    cdef double increase_factor
    cdef unsigned long long int size
    cdef int contains_zero
    cdef long long int mult
    cdef long long int _add
    cdef array.array arr
    
    def __init__(self, start_size=1001, min_factor=1.5, increase_factor=1.2):
      self.__cnt=0
      self.min_factor=min_factor
      self.increase_factor=increase_factor
      self.size=self.ini_array(start_size)
      self.contains_zero=0
      self.mult=random.choice(_primes)
      self._add=random.randint(100, 2000)
      
      
      
    cdef ini_array(self, long long int minimal_size):
        self.arr=array.array('L', [0])
        array.resize(self.arr,minimal_size)
        array.zero(self.arr)
        return minimal_size
            
    cdef get_hash(self, unsigned long long int val):
        return (self.mult*hash(val)+self._add)%self.size
      
    cdef __realocate(self, unsigned long long int new_minimal_size):
        old_arr=self.arr
        
        self.size=self.ini_array(new_minimal_size)
        
        for i in xrange(len(old_arr)):
            if self.arr.data.as_ulongs[i]!=0:
                    self.add(self.arr.data.as_ulongs[i])
            
    def add(self, unsigned long long int val):
        #the special case -> 0, in the array it means empty space
        if val==0:
           self.contains_zero=1
           return -(self.contains_zero-1)
          
        #if there is not enough place -> reallocate   
        if(self.__cnt*self.min_factor>self.size): 
           self.__realocate(int(math.ceil(self.size*self.increase_factor)))
            
        
        #all values except 0:
        cdef unsigned long long int val_hash=self.get_hash(val)
            
        while self.arr.data.as_ulongs[val_hash]:
            if val==self.arr.data.as_ulongs[val_hash]:
                return False #already in the set
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        self.__cnt+=1
        self.arr.data.as_ulongs[val_hash]=val
        return True

    def __contains__(self, unsigned long long int val):
        #the special case -> 0, in the array it means empty space
        if not val:
            return self.contains_zero
        
        #all values except 0:    
        cdef unsigned long long int val_hash=self.get_hash(val)
            
        while self.arr.data.as_ulongs[val_hash]:
            if self.arr.data.as_ulongs[val_hash]==val:
                return True
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        return False
        
    def __len__(self):     
        return self.__cnt+self.contains_zero
        
    def get_preallocated_size(self):
        return len(self.arr)
