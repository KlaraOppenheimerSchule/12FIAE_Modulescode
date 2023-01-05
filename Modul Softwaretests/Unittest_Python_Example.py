# Import

import unittest 

# Fläche von Rechteck und rechtwinkligen Dreieck 

# function calculate area

def flaeche(n,a,b):
    if n == 'dreieck':
        return (a*b/2)
    
    elif n == 'rechteck':
        return (a*b)
    
    else: 
        return 'Error'


#Unittest
class testFlaeche(unittest.TestCase):
    def testequal(self):
        self.assertEqual(flaeche('dreieck',3,2),3)
        self.assertEqual(flaeche('rechteck',3,2),6)
        self.assertEqual(flaeche('dreieck',7,3),10.5)

unittest.main()