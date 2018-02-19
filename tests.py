import unittest
from selenium import webdriver
from pages import *

#https://github.com/gunesmes/page-object-python-selenium/blob/master/testPages.py

class HerokuApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com")

    def test_page_load(self):
        page = MainPage(self.driver)
        self.assertEquals(page.get_title(), "The Internet")

    def test_click_button(self):
        challengingDOMPage = ChallengingDOM(self.driver)
        challengingDOMPage.click_button()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HerokuApp)
    unittest.TextTestRunner(verbosity=2).run(suite)