
import array
import random
import itertools


_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]

class TightHashSet:
    def __init__(self, start_size=10, min_factor=1.5, key_type='i'):
      self.cnt=0
      self.size=start_size
      self.min_factor=min_factor
      self.key_type=key_type
      self.arr=array.array(self.key_type, itertools.repeat(0, self.size))
      self.contains_zero=False
      self.mult=random.choice(_primes)
      self._add=random.randint(100, 2000)
 
    def get_hash(self, val):
        return (self.mult*hash(val)+self._add)%self.size
      
        
    def add(self, val):
        #the special case -> 0, in the array it means empty space
        if not val:
           result=not self.contains_zero
           self.contains_zero=True
           return result
        
        #all values except 0:
        val_hash=self.get_hash(val)
        if self.cnt==self.size:
            raise Exception("No place left")
            
        while self.arr[val_hash]:
            if val==self.arr[val_hash]:
                return False #already in the set
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        self.cnt+=1
        self.arr[val_hash]=val
        return True

    def __contains__(self, val):
        #the special case -> 0, in the array it means empty space
        if not val:
            return self.contains_zero
        
        #all values except 0:    
        val_hash=self.get_hash(val)
        if self.cnt==self.size:
            raise Exception("No place left")
            
        while self.arr[val_hash]:
            if self.arr[val_hash]==val:
                return True
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        return False
        
    def __len__(self):     
        return self.cnt+self.contains_zero
        

