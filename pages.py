from selenium import webdriver
from selenium.webdriver.common.by import By
from base import BasePage

class MainPage(BasePage):
    locator = {
        "BROKEN_IMGS": (By.PARTIAL_LINK_TEXT, 'Broken Images'),
        "Checkboxes": (By.PARTIAL_LINK_TEXT, 'Checkboxes')
    }

    def __init__(self, driver):
        #self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

    def click_broken_images_page(self):
        self.find_element(*self.locator.BROKEN_IMGS).click()
        return BrokenImgsPage(self.driver)


class ChallengingDOM(BasePage):
    locator2 = {
        "BLUE_BUTTON": (By.ID, 'd7934c40-f7d7-0135-6d0d-6e3c0cd0cc18')
    }

    def click_button(self):
        self.find_element(*self.locator2.BLUE_BUTTON).click()