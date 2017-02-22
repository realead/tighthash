from timeit import default_timer as timer


def add_elements(s, n):
    for x in xrange(n):
        s.add(x)
    
def lookup_elements(s, n):
    su=0
    for x in xrange(n):
        if x in s:
          su+=1
    return su  
  

def testing_script(name, collection, sizes=[10**4, 10**5, 10**6, 10**7], N=2):

    print "\n######## testing", name,"##################" 
        
    #add
    for size in sizes:
        for _ in xrange(N):
            try:
              s=collection(sizes*2.0)
            except:
              s=collection()# for default set
              
            start_time=timer()
            add_elements(s, size)
            end_add_time=timer()
            r=lookup_elements(s,size)
            end_lookup_time=timer()
          
        number="10**{0}".format(len(str(size))-1)        
        print number,":",(end_add_time-start_time)/(N*size),"sec per add"
        print number,":",(end_lookup_time-end_add_time)/(N*size),"sec per lookup"
        
        

    print "\n######## done testing", name,"##################\n"  
     
