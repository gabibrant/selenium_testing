from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest

def test_server_connect():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
    driver.close()

def broken_images():

test_server_connect()


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
