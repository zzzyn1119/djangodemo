#! coding=utf-8

import unittest
import time
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
	self.browser.implicitly_wait(3)    

    def tearDown(self):
        self.browser.quit()

    def test_open_url(self):
        self.browser.get('http://localhost:8000')
	time.sleep(3)
	print self.browser.title 
	self.assertIn('Django', self.browser.title)
	#self.fail('Finished the test!')
        #assert 'Django' in browser.title

if __name__=='__main__':
    unittest.main()
