
import array
import random
import math


_primes=[419,421,431,463,467,557,563,569,673,677,683,691,701,709,719,727,733 ,739,743,751,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,947,953,967,971,977,983,991,997,1009,1013]

class THSetIterator:  
    def __init__(self, contains_zero, arr):
        self.__contains_zero=contains_zero
        self.__arr=arr
        self.__it=0
        
        
    def next(self):
        if self.__it==0:
           self.__it+=1
           if self.__contains_zero: 
              return 0
              
        while True:
            if self.__it>len(self.__arr):
                raise StopIteration
            self.__it+=1
            if self.__arr[self.__it-2]!=0:          
                return self.__arr[self.__it-2]


class TightHashSet:
    def __init__(self, capacity=1000, min_factor=1.2, increase_factor=1.2):
      self.__cnt=0
      self.min_factor=max(1.2, min_factor)
      self.key_type='L'
      self.increase_factor=max(1.2, increase_factor)
      self.size=self.ini_array(int(math.ceil(min_factor*capacity)))
      self.contains_zero=False
      self.mult=random.choice(_primes)
      self._add=random.randint(100, 2000)
      
      
    def ini_array(self, minimal_size):
        if minimal_size<100:
            self.arr=array.array(self.key_type, [0])*minimal_size
            return minimal_size
        else:
            repeat=(minimal_size+99)//100
            self.arr=(array.array(self.key_type,[0])*100)*repeat
            return repeat*100
            
    def get_hash(self, val):
        return (self.mult*hash(val)+self._add)%self.size
      
    def __realocate(self, new_minimal_size):
        old_arr=self.arr
        
        self.size=self.ini_array(new_minimal_size)
        
        self.__cnt=0
        for val in old_arr:
           if val:
              self.add(val)
    
    
    def __move_pos(self, pos):
        return 0 if pos==self.size-1 else pos+1
        
    def __find(self, start, item):
        while self.arr[start] and self.arr[start]!=item:
            start=self.__move_pos(start)
        return start
         
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
        
        pos=self.__find(val_hash, val)
        if self.arr[pos]: 
            return False #already in the set
                
        self.arr[pos]=val
        self.__cnt+=1
        return True

    def __contains__(self, val):
        #the special case -> 0, in the array it means empty space
        if not val:
            return self.contains_zero
        
        #all values except 0:    
        val_hash=self.get_hash(val)
        
        pos=self.__find(val_hash, val)
        if self.arr[pos]:
            return True
        return False   
        
    def __len__(self):     
        return self.__cnt+self.contains_zero
        
    def get_preallocated_size(self):
        return len(self.arr)
        
    def discard(self, val):
       if val==0:
             if self.contains_zero:
                self.contains_zero=False
             return
       val_hash=self.get_hash(val)  
       pos=self.__find(val_hash, val)
       if not self.arr[pos]:
            return #not in the set!
            
       self.arr[pos]=0 #delete
       self.__cnt-=1
        
       #reorder the next values
       #we are sure everything is OK only after meeting a 0
       pos =self.__move_pos(pos)
       while self.arr[pos]:
           val=self.arr[pos]
           self.__cnt-=1
           self.arr[pos]=0
           self.add(val)
           pos=self.__move_pos(pos)
           
           
    def __iter__(self):
        return THSetIterator(self.contains_zero, self.arr)
        
    
    
        
        
