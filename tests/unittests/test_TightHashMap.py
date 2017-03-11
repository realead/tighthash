import unittest

import sys
sys.path.append('..')#tighthash
sys.path.append('../uttemplate/uttemplate')

import uttemplate

from tighthash.TightSet  import TightHashMap as PMap

import pyximport; pyximport.install()
from tighthash.ctighthash  import TightHashMap as CMap


@uttemplate.from_templates([PMap, CMap])    
class MapTester(unittest.TestCase):
        
    def template_insert_zero(self,test_class=PMap):
        s=test_class(10)
        self.assertEquals(len(s), 0)
        s[0]=44
        self.assertEquals(len(s), 1)
        self.assertTrue(0 in s)

    def template_insert_no_realoc(self,test_class=PMap):
        s=test_class(10)
        for x in xrange(1,11):
            s[x]=x       
        self.assertEquals(len(s), 10)
        for x in xrange(1,11):
            self.assertTrue(x in s)
            
    def template_insert_no_realoc_with_zero(self,test_class=PMap):
        s=test_class(11)
        for x in xrange(0,11):
            s[x]=x         
        self.assertEquals(len(s), 11)
        for x in xrange(0,11):
            self.assertTrue(x in s)
            
    def template_not_in(self,test_class=PMap):
        s=test_class(11)
        for x in xrange(0,11):
            self.assertFalse(x in s)    
        s[0]=2
        for x in xrange(1,11):
            self.assertFalse(x in s)
        self.assertTrue(0 in s)
        

    def template_insert_with_realoc(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(10):
            s[x]=x       
        self.assertEquals(len(s), 10)
        for x in xrange(10):
            self.assertTrue(x in s)  
            
            
    def template_get_item_zero(self,test_class=PMap):
        s=test_class(4)
        s[0]=100 
        self.assertEquals(s[0], 100)
        s[0]=200
        self.assertEquals(s[0], 200)   
            
            
    def template_get_item_zero_throws(self,test_class=PMap):
        s=test_class(4)
        with self.assertRaises(KeyError) as context:
           x=s[0]
        
        self.assertEquals(0, context.exception.args[0])  
           
    def template_get_item_nonzero(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(1,10):
           s[x]=x+22
        self.assertEquals(len(s), 9)
        for x in xrange(1,10):
           self.assertEquals(s[x], x+22)
           
    def template_get_item_nonzero_throws(self,test_class=PMap):
        s=test_class(4)
        for x in xrange(1,10):
            s[x]=x+22
        self.assertEquals(len(s), 9)
        for x in xrange(22,40):
            with self.assertRaises(KeyError) as context:
                a=s[x]
            self.assertEquals(x, context.exception.args[0])   
            
            
    def template_iterate_with_zero(self, test_class=PMap):
        s=test_class(10)
        for x in xrange(50):
          s[x]=x+33
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        test_list=[]
        for x in s:
            test_list.append((x, s[x]))
            
        self.assertEquals(len(test_list), 50)
        for x in xrange(50):
          self.assertTrue((x, x+33) in test_list)
          
          
          
    def template_iterate_without_zero(self, test_class=PMap):
        s=test_class(10)
        for x in xrange(1,51):
          s[x]=x+44
          self.assertTrue(x in s)
        self.assertEquals(len(s), 50)
        
        test_list=[]
        for x in s:
            test_list.append((x, s[x]))
            
        self.assertEquals(len(test_list), 50)
        for x in xrange(1,51):
          self.assertTrue( (x, x+44) in test_list) 
          
          
    def template_delitem(self, test_class=PMap):
        s=test_class(10)
        for x in xrange(1,11):
          s[x]=x+44
          self.assertTrue(x in s)
        s[0]=33
        
        for x in xrange(1,11):
           del s[x]
           self.assertFalse(x in s)
        
        self.assertTrue(0 in s)
        self.assertEquals(len(s), 1)
               
             
    def template_delitem_zero(self, test_class=PMap):
        s=test_class(10)
        s[0]=0
        self.assertTrue(0 in s)
        del s[0]
        self.assertFalse(0 in s)
        self.assertEquals(len(s), 0)        
            
    def template_delitem_zero_throws(self, test_class=PMap):
        s=test_class(4)
        with self.assertRaises(KeyError) as context:
             del s[0]
        self.assertEquals(0, context.exception.args[0])     
        
    def template_delitem_throws(self, test_class=PMap):
        s=test_class(4)
        for x in xrange(1,11):
          s[x]=x+44
          self.assertTrue(x in s)
        s[0]=33
        
        for x in xrange(22,33):
            with self.assertRaises(KeyError) as context:
                del s[x]
            self.assertEquals(x, context.exception.args[0])   
        
                                                
