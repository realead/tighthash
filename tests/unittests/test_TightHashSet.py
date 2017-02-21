import unittest

import sys
sys.path.append('..')#tighthash
sys.path.append('../uttemplate/uttemplate')

import uttemplate

from tighthash.TightSet  import TightHashSet as PSet

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashSet as CSet


@uttemplate.from_templates([PSet, CSet])    
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
        s=test_class(30)
        self.assertEquals(s.get_preallocated_size(), 30)
        
        
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
        s=test_class(3)
        li=[4,6,77,8]
        self.assertEquals(s.get_preallocated_size(), 3) 
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
        self.assertTrue(s.get_preallocated_size()>3)  
        
        
    def template_realocate_with_zero(self, test_class):
        s=test_class(3)
        li=[4,6,77,8,0]
        self.assertEquals(s.get_preallocated_size(), 3) 
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
        self.assertTrue(s.get_preallocated_size()>3)  
        

    
                     
