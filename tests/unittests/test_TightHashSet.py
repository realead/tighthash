import unittest

import sys
sys.path.append('..')

from tighthash.TightSet  import TightHashSet as PSet

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashSet as CSet

       
class TesterTemplate:
        
    def test_len(self):
        s=self.test_class()
        self.assertEquals(len(s), 0)
        self.assertTrue(s.add(5))
        self.assertEquals(len(s), 1)

    def test_add(self):
        s=self.test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(23))
        self.assertTrue(s.add(123))
        self.assertTrue(s.add(985))
        self.assertEquals(len(s), 4)
        
    def test_in(self):
        s=self.test_class()
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
        
           
    def test_insert_twice(self):
        s=self.test_class()
        self.assertTrue(s.add(5))
        self.assertFalse(s.add(5))
        self.assertEquals(len(s), 1)
        
    def test_insert_negative(self):
        s=self.test_class()
        self.assertTrue(s.add(-5))
        self.assertTrue(s.add(-500000))
        self.assertEquals(len(s), 2)
        
         
    def test_insert_zero(self):
        s=self.test_class()
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),1) 
        self.assertFalse(s.add(0))
        self.assertEquals(len(s),1) 
    
             
    def test_no_zero(self):
        s=self.test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertEquals(len(s),2) 
        self.assertFalse(0 in s)  
        
    def test_has_zero(self):
        s=self.test_class()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),3) 
        self.assertTrue(0 in s)   
 
         
    def test_preallocated_size(self):
        s=self.test_class(30)
        self.assertEquals(s.get_preallocated_size(), 30)
        
        
    def test_dont_count_twice(self):
        s=self.test_class(1)
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertFalse(0 in s)
        self.assertEquals(len(s), 2)  
        
        
    def test_dont_insert_zero(self):
        s=self.test_class(10)
        for z in xrange(1,11):
            self.assertTrue(s.add(z))           
        self.assertFalse(0 in s)    
        
        
    def test_realocate(self):
        s=self.test_class(3)
        li=[4,6,-6,8]
        self.assertEquals(s.get_preallocated_size(), 3) 
        for i in li:
            self.assertTrue(s.add(i))
        for i in li:
            self.assertTrue(i in s)   
        self.assertTrue(s.get_preallocated_size()>3)  
        
        
        
       
class PSetTester(unittest.TestCase, TesterTemplate):  
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.test_class=PSet

       
class CSetTester(unittest.TestCase, TesterTemplate):  
    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.test_class=CSet
    
                     
