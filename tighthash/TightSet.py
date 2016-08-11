
import array
import random
import math


_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]

class TightHashSet:
    def __init__(self, start_size=10, min_factor=1.5, key_type='i', increase_factor=1.2):
      self.__cnt=0
      self.size=start_size
      self.min_factor=min_factor
      self.key_type=key_type
      self.increase_factor=increase_factor
      self.arr=array.array(self.key_type, [0])*self.size
      self.contains_zero=False
      self.mult=random.choice(_primes)
      self._add=random.randint(100, 2000)
 
    def get_hash(self, val):
        return (self.mult*hash(val)+self._add)%self.size
      
    def __realocate(self, new_size):
        old_arr=self.arr
        
        self.size=new_size
        self.arr=array.array(self.key_type, [0])*self.size
        
        for val in old_arr:
            self.add(val)
            
    def add(self, val):
        #the special case -> 0, in the array it means empty space
        if not val:
           result=not self.contains_zero
           self.contains_zero=True
           return result
          
        #if there is not enough place -> reallocate   
        if(self.__cnt*self.min_factor>self.size): 
           self.__realocate(int(math.ceil(self.size*self.increase_factor)))
            
        
        #all values except 0:
        val_hash=self.get_hash(val)
            
        while self.arr[val_hash]:
            if val==self.arr[val_hash]:
                return False #already in the set
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        self.__cnt+=1
        self.arr[val_hash]=val
        return True

    def __contains__(self, val):
        #the special case -> 0, in the array it means empty space
        if not val:
            return self.contains_zero
        
        #all values except 0:    
        val_hash=self.get_hash(val)
            
        while self.arr[val_hash]:
            if self.arr[val_hash]==val:
                return True
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        return False
        
    def __len__(self):     
        return self.__cnt+self.contains_zero
        
    def get_preallocated_size(self):
        return len(self.arr)
