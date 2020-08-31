from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit() 

    def test_can_start_edit_cv(self):
        # The user enters our edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # The user notices the page title and header mention edit
        self.assertIn('Editor', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Editor', header_text)

if __name__ == "__main__":
    unittest.main()