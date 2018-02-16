import pytest

"""
Required package:       pip install pytest-selenium
Execution:              pytest --driver chrome pytest_studies.py
"""

#@pytest.fixture(scope="session")
#def open_url():
#    selenium.get('https://the-internet.herokuapp.com')

"""
def test_url(selenium):
    selenium.get('https://the-internet.herokuapp.com')
    assert "The Internet" in selenium.title

def test_broken_images(selenium):
    selenium.get('https://the-internet.herokuapp.com')
    selenium.find_element_by_partial_link_text('Broken Images').click()
    assert "The Internet" in selenium.title
"""
def test_checkbox(selenium):
    selenium.get('https://the-internet.herokuapp.com')
    selenium.find_element_by_partial_link_text('Checkboxes').click()
    selenium.find_element_by_xpath('//*[@id="checkboxes"]/input[1]').click()
    selenium.find_element_by_xpath('//*[@id="checkboxes"]/input[1]').click()
    selenium.find_element_by_xpath('//*[@id="checkboxes"]/input[1]').click()



