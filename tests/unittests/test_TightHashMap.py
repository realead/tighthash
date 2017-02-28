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
            
            
                                     
