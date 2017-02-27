from timeit import default_timer as timer

import sys

def add_elements(s, n):
    for x in xrange(n):
        s.add(x)
    
def lookup_elements(s, n):
    su=0
    for x in xrange(n):
        if x in s:
          su+=1
    return su  

def delete_nonexisting(s,n):
    for x in xrange(n,2*n):
       s.discard(x)

def delete_elements(s, n):
    for x in xrange(n):
        s.discard(x)
        

def testing_script(name, collection):
  
    size=int(sys.argv[1])

    print "\n######## testing", name,"##################" 
        
    #add
    try:
      s=collection(size) 
    except:
      s=collection()# for default set
     
    number="{0}".format(size)  
    start_time=timer()
    add_elements(s, size)
    end_add_time=timer()
    print number,":",(end_add_time-start_time)/(size),"sec per add"
    
    r=lookup_elements(s,size)
    end_lookup_time=timer()
    print number,":",(end_lookup_time-end_add_time)/(size),"sec per lookup"
    print "Size:", sys.getsizeof(s)
    print "len:", len(s)
    try:
        print "reserved:", s.get_preallocated_size()
    except:
        pass
        
    delete_nonexisting(s, size)
    end_nonexisting_time=timer()
    print number,":",(end_nonexisting_time-end_lookup_time)/(size),"sec per discarding nonexisting"
    
    delete_elements(s, size)
    end_delete_time=timer()
    print number,":",(end_delete_time-end_nonexisting_time)/(size),"sec per discarding existing"
          
            
    

        
       
    print "\n######## done testing", name,"##################\n"  
     
