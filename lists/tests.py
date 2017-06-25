from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.
'''
class SmokeTest(TestCase):
    def test_bad_maths(self):
	self.assertEqual(1+1,3)
'''
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
	found = resolve('/')
	self.assertEqual(found.func, home_page)
	
    def test_home_page_returns_correct_html(self):
	# 创建一个HttpRequest对象
	request = HttpRequest()
	# 将对象传给home_page视图，得到响应
	response = home_page(request)
	self.assertTrue(response.content.startswith(b'<html>'))
	self.assertIn(b'<title>To-Do lists</tilte>',response.content)
	self.assertTrue(response.content.endswith(b'</html>'))

