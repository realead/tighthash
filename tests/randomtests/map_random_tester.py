import random


def are_equal(map1, map2):
    for key in map1:
        if key not in map2:
            return False
        if map1[key]!=map2[key]:
            return False
    for key in map2:
        if key not in map1:
            return False
        if map1[key]!=map2[key]:
            return False
    return True        
           

def test_set(seed, map_type, max_val=10**18):
    random.seed(seed)
    n=random.randint(1,100000)
    s=map_type(capacity=random.randint(1,n*2), min_factor=1.0+random.random(), increase_factor=1.0+random.random())
    control={}
    
    ##test add:
    for i in xrange(n):
        key=random.randint(0, max_val)
        val=random.randint(0, max_val)
        s[key]=val
        control[key]=val
     
    if len(s)!=len(control):
        return (False, "different lengths")
     
    ##test in:
    if not are_equal(s, control):
        return (False, "mismatch after insert")
     
     
    for i in xrange(n):
         key=random.randint(0, max_val)
         if (key in s) != (key in control):
            return (False, "query mismatch")
         if (key in s) and s[key]!=control[key]:       
            return (False, "query result mismatch")
            
         
            
            
    ##test delete
    for i in xrange(n):
         key=random.randint(0, max_val)
         raised_S=False
         try:
           del s[key]
         except KeyError:
           raised_S=True
         raised_C=False
         try:
           del control[key]
         except KeyError:
            raised_C=True
         if raised_S!=raised_C:
            return (False, "raised mismatch!");
         
            
    if not are_equal(s, control):
        return (False, "mismatch after delete1")
        
        
    to_delete=[ x for x,_ in zip(control, xrange(n//2))]
    for d in to_delete:
        del s[d]
        del control[d]
        
     
    if not are_equal(s, control):
        return (False, "mismatch after delete1")
        
    return (True, "Ok")
     
#test cases:


def test_cases(map_type):

    cnt=0
    wrong=[]
    #small numbers
    for seed in xrange(50):
        cnt+=1
        res, error=test_set(seed, map_type, 100)
        if not res:
            wrong.append(error)           
    print "small numbers done for", str(map_type)
                  
    #medium numbers
    for seed in xrange(100,200):
        cnt+=1
        res, error=test_set(seed, map_type, 10**7)
        if not res:
            wrong.append(error)  
    print "medium numbers done for", str(map_type)  
            
    #large numbers
    for seed in xrange(1000,1400):
        cnt+=1
        res, error=test_set(seed, map_type, 10**18)
        if not res:
            wrong.append(error)
    print "large numbers done for", str(map_type) 
            
    if wrong:
        print "Errors"
        print wrong.join()
        return (len(wrong), cnt)
    return (0, cnt)
        
        
import sys
sys.path.append('..')

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashMap as cmap

print "Testing cmap..."
wrong, cnt=test_cases(cmap)
if not wrong:
    print "cmap tests are all %d OK!"%cnt
else:
    print "%d errors for %d cmap tests!"%(wrong, cnt)
    
    
from tighthash.TightSet  import TightHashMap as pmap

print "Testing pmap..."
wrong, cnt=test_cases(pmap)
if not wrong:
    print "pmap tests are all %d OK!"%cnt
else:
    print "%d errors for %d pmap tests!"%(wrong, cnt)        
        
     
