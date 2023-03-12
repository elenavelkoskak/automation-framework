import unittest
from selenium import webdriver
from automationframework.config.config import *
from automationframework.pages.CompanyPage import CompanyPage


class TestCompanyPage(unittest.TestCase):
    option_value = "Anywhere"

    def setUp(self) -> None:
        if BROWSER == "chrome":
            self.driver = webdriver.Chrome()
        elif BROWSER == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.get(BASEURL)
        self.company_page = CompanyPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_company_page(self):
        self.company_page.click_company_button()
        company_url = self.driver.current_url
        assert company_url == "https://www.musala.com/company/"
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert self.company_page.check_leadership_section() == "Leadership"
        self.company_page.click_facebook_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        facebook_url = self.driver.current_url
        assert facebook_url == "https://www.facebook.com/MusalaSoft?fref=ts"
        assert self.company_page.is_fb_picture_displayed()






