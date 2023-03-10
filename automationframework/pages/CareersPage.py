from selenium.webdriver.common.by import By
from automationframework.pages.BasePage import BasePage
from selenium.webdriver.support.ui import Select


class CareersPage(BasePage):
    CAREERS_BUTTON = (By.LINK_TEXT, "CAREERS")
    OPEN_POSITIONS_BUTTON = (By.CLASS_NAME, "contact-label-code")
    ALL_LOCATION_DROPDOWN = (By.ID, "get_location")
    CHOOSE_POSITION_BY_NAME = (By.XPATH, "//*[@id='content']/section/div[2]/article[1]/div/a/div/div[2]/img")
    MAIN_SECTIONS = (By.CLASS_NAME, "content-title")
    APPLY_BUTTON = (By.XPATH, "//input[@value='Apply']")
    NAME_FIELD = (By.ID, "cf-1")
    EMAIL_FIELD = (By.ID, "cf-2")
    PHONE_FIELD = (By.ID, "cf-3")
    CHOOSE_FILE_FIELD = (By.ID, "cf-4")
    SEND_BUTTON = (By.XPATH, "//input[@value='Send']")
    INVALID_MESSAGES = (By.XPATH, "//span[@class='wpcf7-not-valid-tip']")
    POSITION_NAME = (By.CLASS_NAME, "card-jobsHot__title")
    LINKS = (By.CLASS_NAME, "card-jobsHot__link")

    def careersButton(self):
        careers_button = self.driver.find_element(*self.CAREERS_BUTTON)
        careers_button.click()

    def openPositionsButton(self):
        open_positions_button = self.driver.find_element(*self.OPEN_POSITIONS_BUTTON)
        open_positions_button.click()

    def locationDropdown(self, location_value):
        select = Select(self.driver.find_element(*self.ALL_LOCATION_DROPDOWN))
        select.select_by_value(location_value)

    def choosePosition(self):
        links = self.driver.find_elements(By.CLASS_NAME, "card-jobsHot__link")
        for link in links:
            text = link.find_element(By.CSS_SELECTOR, "div div h2").text
            if text == "Senior Java Developer":
                link.click()
                break

    def checkMainSections(self):
        main_sections = ["General description", "Requirements", "Responsibilities", "What we offer"]
        sections = self.driver.find_elements(*self.MAIN_SECTIONS)
        for section in sections:
            section_name = section.find_element(By.CSS_SELECTOR, "h2").text
            if section_name not in main_sections:
                return False
        return True

    def selectLocation(self):
        location = self.driver.find_element(*self.SELECT_LOCATION)
        location.click()

    def findApplyButton(self):
        element = self.driver.find_element(*self.APPLY_BUTTON)
        return element

    def setName(self, name):
        name_field = self.driver.find_element(*self.NAME_FIELD)
        name_field.send_keys(name)

    def setMail(self, email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

    def setPhone(self, phone):
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.send_keys(phone)

    def uploadCV(self, cv_url):
        choose_file = self.driver.find_element(*self.CHOOSE_FILE_FIELD)
        choose_file.clear()
        choose_file.send_keys(cv_url)

    def fillApplyForm(self, info: dict):
        self.setName(info.get("name"))
        self.setMail(info.get("email"))
        self.setPhone(info.get("phone"))
        self.uploadCV(info.get("cv"))

    def clickSendButton(self):
        send_button = self.driver.find_element(*self.SEND_BUTTON)
        self.driver.execute_script("arguments[0].click();", send_button)

    def validateInvalidMessages(self):
        invalid_messages = self.driver.find_elements(*self.INVALID_MESSAGES)
        messages = ["The e-mail address entered is invalid.", "The telephone number is invalid."]
        for message in invalid_messages:
            if message.text not in messages:
                return False
        return True

    def extract_position_data(self, location: str):
        positions = self.driver.find_elements(*self.POSITION_NAME)
        links = self.driver.find_elements(*self.LINKS)

        print(location)
        for (position, link) in zip(positions, links):
            link_href = link.get_attribute("href")
            print(f"Position: {position.text}")
            print(f"More info: {link_href}")











