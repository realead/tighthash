
import array
import random

_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]

class TightHashSet:
    def __init__(self, start_size=10, min_factor=1.5, key_type='i'):
      self.cnt=0
      self.size=start_size
      self.min_factor=min_factor
      self.key_type=key_type
      self.arr=array.array(self.key_type, self.size)
      self.mult=randome.choice(_primes)
      self.add=random.randint(100, 2000)
 
    def get_hash(self, val):
        return (self.mult*hash(val)+self.add)%self.size
      
        
    def add(self, val):
        val_hash=self.get_hash(val)
        if self.cnt==self.size:
            raise Exception("No place left")
            
        while not self.arr[val_hash]:
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        self.cnt+=1
        self.arr[val_hash]=val

    def __contains__(self, val):
        val_hash=self.get_hash(val)
        if self.cnt==self.size:
            raise Exception("No place left")
            
        while not self.arr[val_hash]:
            if self.arr[val_hash]==val:
                return True
            if val_hash==self.size-1:
                val_hash=0
            else: val_hash+=1
        
        return False
        
    def __contains__(self):
        
        return self.cnt
        

