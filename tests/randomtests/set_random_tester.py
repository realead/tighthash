import random


def are_equal(set1, set2):
    for key in set1:
        if key not in set2:
            return False
    for key in set2:
       if key not in set1:
            return False
    return True        
           

def test_set(seed, set_type, max_val=10**18):
    random.seed(seed)
    n=random.randint(1,100000)
    s=set_type(capacity=random.randint(1,n*2), min_factor=1.0+random.random(), increase_factor=1.0+random.random())
    control=set()
    
    ##test add:
    for i in xrange(n):
        key=random.randint(0, max_val)
        s.add(key)
        control.add(key)
     
    if len(s)!=len(control):
        return (False, "different lengths")
     
    ##test in:
    if not are_equal(s, control):
        return (False, "mismatch after insert")
     
     
    for i in xrange(n):
         key=random.randint(0, max_val)
         if (key in s) != (key in control):
            return (False, "query mismatch")
         
            
            
    ##test delete
    for i in xrange(n):
         key=random.randint(0, max_val)
         s.discard(key)
         control.discard(key)
            
    if not are_equal(s, control):
        return (False, "mismatch after delete1")
        
        
    to_delete=[ x for x,_ in zip(control, xrange(n//2))]
    for d in to_delete:
        s.discard(d)
        control.discard(d)
        
     
    if not are_equal(s, control):
        return (False, "mismatch after delete1")
        
    return (True, "Ok")
     
#test cases:


def test_cases(set_type):

    cnt=0
    wrong=[]
    #small numbers
    for seed in xrange(50):
        cnt+=1
        res, error=test_set(seed, set_type, 100)
        if not res:
            wrong.append(error)           
    print "small numbers done for", str(set_type)
                  
    #medium numbers
    for seed in xrange(100,200):
        cnt+=1
        res, error=test_set(seed, set_type, 10**7)
        if not res:
            wrong.append(error)  
    print "medium numbers done for", str(set_type)  
            
    #large numbers
    for seed in xrange(1000,1400):
        cnt+=1
        res, error=test_set(seed, set_type, 10**18)
        if not res:
            wrong.append(error)
    print "large numbers done for", str(set_type) 
            
    if wrong:
        print "Errors"
        print wrong.join()
        return (len(wrong), cnt)
    return (0, cnt)
        
        
import sys
sys.path.append('..')

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashSet as cset


print "Testing cset..."
wrong, cnt=test_cases(cset)
if not wrong:
    print "cset tests are all %d OK!"%cnt
else:
    print "%d errors for %d cset tests!"%(wrong, cnt)
    
    
    
from tighthash.TightSet  import TightHashSet as pset
print "Testing pset..."
wrong, cnt=test_cases(pset)
if not wrong:
    print "pset tests are all %d OK!"%cnt
else:
    print "%d errors for %d pset tests!"%(wrong, cnt)   
    
        
        
     
