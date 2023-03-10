import unittest
from selenium import webdriver
from automationframework.config.config import *
from automationframework.pages.CareersPage import CareersPage


class TestCareersPage(unittest.TestCase):
    def setUp(self) -> None:
        if BROWSER == "chrome":
            self.driver = webdriver.Chrome()
        elif BROWSER == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.get(BASEURL)
        self.careers_page = CareersPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_open_position_options(self):
        path_to_file = "C:/Users/Home/PycharmProjects/AutomationFramework/automationframework/data"
        location_value = "Anywhere"
        musala_join_us = "https://www.musala.com/careers/join-us/"
        scroll = "window.scrollTo(0,{})"
        apply_info = {
            "name": "name1",
            "email": "email1.com",
            "phone": "123abc456",
            "cv": f"{path_to_file}/TestCV.pdf"
        }
        self.careers_page.careersButton()
        self.careers_page.openPositionsButton()
        join_us_url = self.driver.current_url
        assert join_us_url == musala_join_us
        self.careers_page.locationDropdown(location_value)
        self.driver.execute_script(scroll.format(300))
        self.careers_page.choosePosition()
        self.driver.execute_script(scroll.format(600))
        assert self.careers_page.checkMainSections()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        apply_button = self.careers_page.findApplyButton()
        if apply_button:
            assert True
        self.driver.execute_script("arguments[0].click();", apply_button)

        # Fill in apply form
        self.careers_page.fillApplyForm(apply_info)
        self.careers_page.clickSendButton()
        assert self.careers_page.validateInvalidMessages()

    def test_positions_by_city(self):
        locations = ["Skopje", "Sofia"]
        self.careers_page.careersButton()
        self.careers_page.openPositionsButton()
        self.careers_page.locationDropdown(locations[0])
        self.careers_page.extract_position_data(locations[0])
        self.careers_page.locationDropdown(locations[1])
        self.careers_page.extract_position_data(locations[1])








