from cpython cimport array
import array
import random
import math


_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]


cdef class THSetIterator:
    cdef int __contains_zero
    cdef array.array __arr
    cdef unsigned long long int __it
    cdef unsigned long long int __size
    
    def __init__(self, contains_zero, arr):
        self.__contains_zero=contains_zero
        self.__arr=arr
        self.__size=len(arr)
        self.__it=0
        
        
    def __next__(self):
        if self.__it==0:
           self.__it+=1
           if self.__contains_zero==1: 
              return 0
              
        while True:
            if self.__it>self.__size:
                raise StopIteration
            self.__it+=1
            if self.__arr.data.as_ulongs[self.__it-2]!=0:          
                return self.__arr.data.as_ulongs[self.__it-2]
        
#creates array of the given size and initializes it to 0       
cdef create_arr(size):
    cdef array.array arr
    arr=array.array('L', [0])
    array.resize(arr, size)
    array.zero(arr)
    return arr
    
    
cdef class TightHashBase:
    cdef unsigned long long int cnt
    cdef double min_factor
    cdef double increase_factor
    cdef unsigned long long int size
    cdef int contains_zero
    cdef long long int mult
    cdef long long int _add
    cdef array.array arr
    
    def __init__(self,  capacity=1001, min_factor=1.2, increase_factor=1.2):
        self.cnt=0
        self.min_factor=max(1.2, min_factor)
        self.increase_factor= max(1.2, increase_factor)
        self.size=int(math.ceil(capacity*self.min_factor))
        self.arr=create_arr(self.size)
        self.contains_zero=0
        self.mult=random.choice(_primes)
        self._add=random.randint(100, 2000)  
        
    cdef move_pos(self, unsigned long long int pos):
        return 0 if pos==self.size-1 else pos+1
      
    cdef find(self, unsigned long long int start, unsigned long long int item):
        while self.arr.data.as_ulongs[start] and self.arr.data.as_ulongs[start]!=item:
            start=self.move_pos(start)
        return start 
      
    cdef get_hash(self, unsigned long long int val):
        return (self.mult*hash(val)+self._add)%self.size
               
    def __iter__(self):
        return THSetIterator(self.contains_zero, self.arr)      
        
    def __len__(self):     
        return self.cnt+self.contains_zero
        
    def get_preallocated_size(self):
        return len(self.arr)
              

    def __contains__(self, unsigned long long int val):
        #the special case -> 0, in the array it means empty space
        if not val:
            return self.contains_zero
        
        #all values except 0:    
        cdef unsigned long long int val_hash=self.get_hash(val)
        val_hash=self.find(val_hash, val)   
        
        if self.arr.data.as_ulongs[val_hash]==val:
            return True
        return False

cdef class TightHashSet(TightHashBase):
    
    def __init__(self,  capacity=1001, min_factor=1.2, increase_factor=1.2):
        TightHashBase.__init__(self, capacity, min_factor, increase_factor)
    

      
    cdef __realocate(self, unsigned long long int new_minimal_size):
        old_arr=self.arr
        
        self.arr=create_arr(new_minimal_size)
        self.size=len(self.arr)
        
        self.cnt=0
        for i in xrange(len(old_arr)):
            if old_arr.data.as_ulongs[i]!=0:
                    self.add(old_arr.data.as_ulongs[i])
            
    def add(self, unsigned long long int val):
        #the special case -> 0, in the array it means empty space
        if val==0:
            if self.contains_zero==1:
                return False
            else:
                self.contains_zero=1
                return True
          
        #if there is not enough place -> reallocate   
        if(self.cnt*self.min_factor>self.size): 
           self.__realocate(int(math.ceil(self.size*self.increase_factor)))
            
        
        #all values except 0:
        cdef unsigned long long int val_hash=self.get_hash(val)
        val_hash=self.find(val_hash, val)
        if self.arr.data.as_ulongs[val_hash]:
            return False #already in the set
        
        self.arr.data.as_ulongs[val_hash]=val
        self.cnt+=1
        return True
        
        
    def discard(self, unsigned long long int val):
       if val==0:
             if self.contains_zero==1:
                self.contains_zero=0
             return
       cdef unsigned long long int val_hash=self.get_hash(val)  
       cdef unsigned long long int pos=self.find(val_hash, val)
       if not self.arr.data.as_ulongs[pos]:
            return #not in the set!
            
       self.arr.data.as_ulongs[pos]=0 #delete
       self.cnt-=1
        
       #reorder the next values
       #we a sure everything is OK only after meeting a 0
       pos =self.move_pos(pos)
       while self.arr.data.as_ulongs[pos]:
           val=self.arr.data.as_ulongs[pos]
           self.cnt-=1
           self.arr.data.as_ulongs[pos]=0
           self.add(val)
           pos=self.move_pos(pos)
           
           
        
  
        
        
        
