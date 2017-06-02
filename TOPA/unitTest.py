import unittest
import re
#import views

class TestAirline(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    #def test_convertirFecha(array):
    	#for i in array:
    		#fecha=array[i]

    #def test_post(self):
    #	data=views.ejemplo
    #	print data.origin

if __name__ == '__main__':
    unittest.main()
