import requests
from selenium.webdriver.common.by import By
from automationframework.pages.BasePage import BasePage


class CompanyPage(BasePage):
    COMPANY_BUTTON = (By.LINK_TEXT, "COMPANY")
    LEADERSHIP_SECTION = (By.XPATH, "//div[@class='cm-content']//h2")
    FACEBOOK_LINK = (By.CLASS_NAME, "musala-icon-facebook")
    FACEBOOK_PROFILE_DIV = (By.CSS_SELECTOR, "div[class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']")
    FIND_PROFILE_PICTURE = (By.CSS_SELECTOR, "svg g image")

    def click_company_button(self):
        company_button = self.driver.find_element(*self.COMPANY_BUTTON)
        self.driver.execute_script("arguments[0].click();", company_button)

    def check_leadership_section(self):
        return self.driver.find_element(*self.LEADERSHIP_SECTION).text

    def click_facebook_link(self):
        facebook_link = self.driver.find_element(*self.FACEBOOK_LINK)
        self.driver.execute_script("arguments[0].click();", facebook_link)

    def is_fb_picture_displayed(self):
        profile_picture_link = self.driver.find_element(*self.FACEBOOK_PROFILE_DIV)
        image = profile_picture_link.find_element(*self.FIND_PROFILE_PICTURE).get_attribute("xlink:href")
        if requests.get(image).content:
            return True
        return False

