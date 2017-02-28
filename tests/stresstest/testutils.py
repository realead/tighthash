from timeit import default_timer as timer

import sys

def add_elements(s, n):
    for x in xrange(n):
        s.add(x)
 
def lookup_nonexisting(s, n):
    su=0
    for x in xrange(n):
        if x in s:
          su+=1
    return su   
    
def lookup_elements(s, n):
    su=0
    for x in xrange(n):
        if x in s:
          su+=1
    return su 
    
def iterate_through(s):
    su=0
    for x in s:
        su+=x
    return su   

def delete_nonexisting(s,n):
    for x in xrange(n,2*n):
       s.discard(x)

def delete_elements(s, n):
    for x in xrange(n):
        s.discard(x)
        
def stoptime(fun, n, label):
    start_time=timer()
    fun()
    end_time=timer()
    print n,":",(end_time-start_time)/n,"sec per", label
        

def testing_script(name, collection):
  
    size=int(sys.argv[1])

    print "\n######## testing", name,"##################" 
        
    #add
    try:
      s=collection(size) 
    except:
      s=collection()# for default set
     

    stoptime(lambda s=s, size=size : add_elements(s,size), size, "add")
    stoptime(lambda s=s : iterate_through(s), size, "iterating through")
    stoptime(lambda s=s, size=size : lookup_nonexisting(s,size), size, "lookup nonexisting")
    stoptime(lambda s=s, size=size : lookup_elements(s,size), size, "lookup existing")
    stoptime(lambda s=s, size=size : delete_nonexisting(s,size), size, "discard nonexisting")
    stoptime(lambda s=s, size=size : delete_elements(s,size), size, "discard existing")
    
    
    print "\n######## done testing", name,"##################\n"  
     
