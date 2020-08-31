from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit() 

    def test_can_start_edit_cv_page(self):
        # The user enters our edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # The user notices the page title and header mention edit
        self.assertIn('Editor', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Editor', header_text)

    def test_can_edit_cv_personal_profile(self):
        # The user enters our edit page
        self.browser.get('http://127.0.0.1:8000/cv/edit/')

        # The user is invited to edit their personal profile
        inputbox = self.browser.find_element_by_id('id_personal_profile')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter Personal Profile'
        )

        # The user types a brief personal profile
        inputbox.send_keys('I am Shahram and I am passionate about...')  

        # When the user hits enter, the page updates, the CV page must display 
        # the new personal profile
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        self.browser.get('http://127.0.0.1:8000/cv/edit/')
        p = self.browser.find_element_by_id('id_personal_profile')
        self.assertTrue(
            any(p.text == 'I am Shahram and I am passionate about...' for row in rows)
        )

if __name__ == "__main__":
    unittest.main()