import unittest

import sys
sys.path.append('..')#tighthash
sys.path.append('../uttemplate/uttemplate')

import uttemplate

from tighthash.TightSet  import TightHashMap as PMap

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashSet as CSet


#@uttemplate.from_templates([PSet, CSet])    
class MapTester(unittest.TestCase):
        
    def test_insert_zero(self,test_class=PMap):
        s=test_class(10)
        self.assertEquals(len(s), 0)
        s[0]=44
        self.assertEquals(len(s), 1)
        self.assertTrue(0 in s)

    def test_insert_no_realoc(self,test_class=PMap):
        s=test_class(10)
        for x in xrange(1,11):
            s[x]=x       
        self.assertEquals(len(s), 10)
        for x in xrange(1,11):
            self.assertTrue(x in s)
            
    def test_insert_no_realoc_with_zero(self,test_class=PMap):
        s=test_class(11)
        for x in xrange(0,11):
            s[x]=x         
        self.assertEquals(len(s), 11)
        for x in xrange(0,11):
            self.assertTrue(x in s)
            
    def test_not_in(self,test_class=PMap):
        s=test_class(11)
        for x in xrange(0,11):
            self.assertFalse(x in s)    
        s[0]=2
        for x in xrange(1,11):
            self.assertFalse(x in s)
        self.assertTrue(0 in s)
        

    def test_insert_with_realoc(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(10):
            s[x]=x       
        self.assertEquals(len(s), 10)
        for x in xrange(10):
            self.assertTrue(x in s)  
            
            
    def test_get_item_zero(self,test_class=PMap):
        s=test_class(4)
        s[0]=100 
        self.assertEquals(s[0], 100)
        s[0]=200
        self.assertEquals(s[0], 200)   
            
            
    def test_get_item_zero_throws(self,test_class=PMap):
        s=test_class(4)
        with self.assertRaises(KeyError) as context:
           x=s[0]
        
        self.assertEquals(0, context.exception.args[0])  
           
    def test_get_item_nonzero(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(1,10):
           s[x]=x+22
        self.assertEquals(len(s), 9)
        for x in xrange(1,10):
           self.assertEquals(s[x], x+22)
           
    def test_get_item_nonzero_throws(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(1,10):
            s[x]=x+22
        self.assertEquals(len(s), 9)
        for x in xrange(22,40):
            with self.assertRaises(KeyError) as context:
                a=s[x]
            self.assertEquals(x, context.exception.args[0])      
                                              
