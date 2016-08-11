import unittest

import sys
sys.path.append('..')

from tighthash.TightSet  import TightHashSet as Set

       
class ThightHashSetTester(unittest.TestCase):
        
    def test_len(self):
        s=Set()
        self.assertEquals(len(s), 0)
        self.assertTrue(s.add(5))
        self.assertEquals(len(s), 1)

    def test_add(self):
        s=Set()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(23))
        self.assertTrue(s.add(123))
        self.assertTrue(s.add(985))
        self.assertEquals(len(s), 4)
        
    def test_in(self):
        s=Set()
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
        s=Set()
        self.assertTrue(s.add(5))
        self.assertFalse(s.add(5))
        self.assertEquals(len(s), 1)
        
    def test_insert_negative(self):
        s=Set()
        self.assertTrue(s.add(-5))
        self.assertTrue(s.add(-500000))
        self.assertEquals(len(s), 2)
        
         
    def test_insert_zero(self):
        s=Set()
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),1) 
        self.assertFalse(s.add(0))
        self.assertEquals(len(s),1) 
    
             
    def test_no_zero(self):
        s=Set()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertEquals(len(s),2) 
        self.assertFalse(0 in s)  
        
    def test_has_zero(self):
        s=Set()
        self.assertTrue(s.add(5))
        self.assertTrue(s.add(7))
        self.assertTrue(s.add(0))
        self.assertEquals(len(s),3) 
        self.assertTrue(0 in s)   
 
         
    def test_preallocated_size(self):
        s=Set(30)
        self.assertEquals(s.get_preallocated_size(), 30)
        
        
                     
