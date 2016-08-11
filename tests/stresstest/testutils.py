from timeit import default_timer as timer

def add_elements(n, collection):
    s=collection()
    for x in xrange(n):
        s.add(x)
    return s
    
def lookup_elements(s, n):
    su=0
    for x in xrange(n):
        if x in s:
          su+=1
    return su  
  

def testing_script(name, collection, sizes=[10**4, 10**5, 10**6], N=2):

    print "\n######## testing", name,"##################" 
        
    #add
    for size in sizes:
        start_time=timer()
        N=2
        for _ in xrange(N):
            start_time=timer()
            s=add_elements(size, collection)
            end_add_time=timer()
            r=lookup_elements(s,size)
            end_lookup_time=timer()
          
        number="10**{0}".format(len(str(size))-1)        
        print number,":",(end_add_time-start_time)/(N*size),"sec per add"
        print number,":",(end_lookup_time-end_add_time)/(N*size),"sec per lookup"
        
        

    print "\n######## done testing", name,"##################\n"  
     
