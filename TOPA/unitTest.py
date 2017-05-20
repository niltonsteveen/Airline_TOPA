import unittest
import re
#import views

class TestAirline(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_email(self):
    	email="jtorresv232@gmail.com"
    	self.assertEqual('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower())

    #def test_post(self):
    #	data=views.ejemplo
    #	print data.origin

if __name__ == '__main__':
    unittest.main()