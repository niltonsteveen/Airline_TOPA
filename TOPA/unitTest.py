import unittest
import re
from datetime import datetime, date, time, timedelta
import calendar
#import views

class TestAirline(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

	def test_fecha(self):
        fecha=date.today() - timedelta(days=2)
        fechaStr="%d-%m-%Y"
        cadena=fecha.strftime(fechaStr)
        esperada="03-06-2017"
        self.assertEqual(cadena,esperada)


    #def test_convertirFecha(array):
    	#for i in array:
    		#fecha=array[i]

    #def test_post(self):
    #	data=views.ejemplo
    #	print data.origin

if __name__ == '__main__':
    unittest.main()
