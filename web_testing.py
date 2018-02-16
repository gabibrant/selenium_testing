from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest

class heroku_testing:

    def test_open_url(url, title):
        browser = webdriver.Chrome()
        browser.get(url)
        assert title in browser.title
        browser.close()

    test_open_url("https://the-internet.herokuapp.com", "The Internet")



"""
class front_end_testing():
    def setup(self):
        self.driver = webdriver.Chrome()

    def web_testing.py():


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")
assert "The Internet" in driver.title
driver.close()



elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""
