#! coding=utf-8

import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
	self.browser.implicitly_wait(3)    

    def tearDown(self):
        self.browser.quit()

    def test_open_url(self):
        self.browser.get('http://localhost:8000')
	#time.sleep(3)
	#print self.browser.title 
	self.assertIn('To-Do', self.browser.title)
	header_text = self.browser.find_element_by_tag_name('h1').text
	self.assertIn('To-Do', header_text)
	#self.fail('Finished the test!')

        inputbox = self.broser.find_element_by_id('id_new_item')
	self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item)
	inputbox.send_keys('Buy peacock feathers')
	inputbox.send_keys(Keys.ENTER)
	
	table = self.browser.find_element_by_id('id_list_table')
	rows = table.find_element_by_tag_name('tr')
	self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))
	self.fail('Finish the test!')
	

	
	
				

if __name__=='__main__':
    unittest.main()
