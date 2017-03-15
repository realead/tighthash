import unittest

import sys
sys.path.append('..')#tighthash
sys.path.append('../uttemplate/uttemplate')

import uttemplate

from tighthash  import pset, cset

@uttemplate.from_templates([pset, cset])    
class TesterTemplate(unittest.TestCase):
        
    def template_len(self,test_class):
        s=test_class()
        self.assertEquals(len(s), 0)
        self.assertTrue(s.add(5))
        self.assertEquals(len(s), 1)

    def template_add(self, test_class):
        s=test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(23))
        self.assertTrue(s.add(123))
        self.assertTrue(s.add(985))
        self.assertEquals(len(s), 4)
        
    def template_in(self, test_class):
        s=test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(23))
        self.assertTrue(s.add(123))
        self.assertTrue(s.add(985))
        self.assertEquals(len(s), 4)
        self.assertTrue(5 in s)
        self.assertTrue(23 in s)
        self.assertTrue(123 in s)
        self.assertTrue(985 in s)
        self.assertFalse(4 in s)
    
    def template_contains_zero(self, test_class):
        s=test_class(100)
        li=[3,4,5,0]
        for e in li: 
           self.assertTrue(s.add(e))
        for e in li: 
           self.assertTrue(e in s)   
           
    def template_insert_twice(self, test_class):
        s=test_class()
        self.assertTrue(s.add(5))
        self.assertFalse(s.add(5))
        self.assertEquals(len(s), 1)
        
    def template_insert_negative(self, test_class):
        s=test_class()
        with self.assertRaises(OverflowError) as context:
           s.add(-5)   
        with self.assertRaises(OverflowError) as context:
           s.add(-500000)
        self.assertEquals(len(s), 0)
        
         
    def template_insert_zero(self, test_class):
        s=test_class()
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),1) 
        self.assertFalse(s.add(0))
        self.assertEquals(len(s),1) 
    
             
    def template_no_zero(self, test_class):
        s=test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertEquals(len(s),2) 
        self.assertFalse(0 in s)  
        
    def template_has_zero(self, test_class):
        s=test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),3) 
        self.assertTrue(0 in s)   
 
         
    def template_preallocated_size(self, test_class):
        s=test_class(30, min_factor=1.499)
        self.assertEquals(s.get_preallocated_size(), 45)
        
        
    def template_dont_count_twice(self, test_class):
        s=test_class(1)
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertFalse(0 in s)
        self.assertEquals(len(s), 2)  
        
        
    def template_dont_insert_zero(self, test_class):
        s=test_class(10)
        for z in xrange(1,11):
            self.assertTrue(s.add(z))           
        self.assertFalse(0 in s)    
        
        
    def template_realocate(self, test_class):
        s=test_class(1, min_factor=1.5)
        li=[4,6,77,8]
        self.assertEquals(s.get_preallocated_size(), 2) 
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
        self.assertTrue(s.get_preallocated_size()>2) 
        self.assertTrue(s.get_preallocated_size()<6) #not too many! 
       
        
    def template_realocate_with_zero(self, test_class):
        s=test_class(1, min_factor=1.5)
        li=[4,6,77,8,0]
        self.assertEquals(s.get_preallocated_size(),2) 
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
        self.assertTrue(s.get_preallocated_size()>2) 
        self.assertTrue(s.get_preallocated_size()<6) #not too many
        

    def template_minimal_increase(self, test_class):
        s=test_class(1,increase_factor=1.0)
        li=[4,6,77,8,0]
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
    

    def template_minimal_min_factor(self, test_class):
        s=test_class(1,min_factor=1.0)
        li=[4,6,77,8,0]
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)  
            
            
    def template_reserved_for(self, test_class):
        N=1000
        s=test_class(N, min_factor=2.0)
        reserved_number=s.get_preallocated_size();
        for x in xrange(1,N+1):
          s.add(x)
        self.assertEquals(s.get_preallocated_size(), reserved_number)#there was no need to rehash!     
        
            
            
    def template_reserved_for_right_min(self, test_class):
        N=101
        s=test_class(N, min_factor=1.0)
        reserved_number=s.get_preallocated_size();
        for x in xrange(1,N+1):
          s.add(x)
        self.assertEquals(s.get_preallocated_size(), reserved_number)#there was no need to rehash!     
        
        
    def template_discard(self, test_class):
        s=test_class(10)
        for x in xrange(1,11):
          s.add(x)
          self.assertTrue(x in s)
        s.add(0)
        
        for x in xrange(1,11):
          s.discard(x)
          self.assertFalse(x in s)
        
        self.assertTrue(0 in s)
        self.assertEquals(len(s), 1)
               
             
    def template_discard_zero(self, test_class):
        s=test_class(10)
        s.add(0)
        self.assertTrue(0 in s)
        s.discard(0)
        self.assertFalse(0 in s)
        self.assertEquals(len(s), 0)
        
                
    def template_discard_all(self, test_class):
        s=test_class(10)
        for x in xrange(50):
          s.add(x)
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        for x in reversed(xrange(25)):
          s.discard(x)
          self.assertFalse(x in s)
        
        self.assertEquals(len(s), 25)
        for x in xrange(25,50):
            self.assertTrue(x in s)
           
        
    def template_discard_nonexisting(self, test_class):
        s=test_class(10)
        for x in xrange(50):
          s.add(x)
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        for x in reversed(xrange(50,75)):
          s.discard(x)
          self.assertFalse(x in s)
        
        self.assertEquals(len(s), 50)
        for x in xrange(50):
            self.assertTrue(x in s)                   
        
        
    def template_iterate_with_zero(self, test_class):
        s=test_class(10)
        for x in xrange(50):
          s.add(x)
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        test_list=[]
        for x in s:
            test_list.append(x)
            
        self.assertEquals(len(test_list), 50)
        for x in xrange(50):
          self.assertTrue(x in test_list)
          
          
          
    def template_iterate_without_zero(self, test_class):
        s=test_class(10)
        for x in xrange(1,51):
          s.add(x)
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        test_list=[]
        for x in s:
            test_list.append(x)
            
        self.assertEquals(len(test_list), 50)
        for x in xrange(1,51):
          self.assertTrue(x in test_list)         
                             
