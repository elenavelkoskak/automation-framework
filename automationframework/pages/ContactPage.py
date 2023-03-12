from selenium.webdriver.common.by import By
from automationframework.pages.BasePage import BasePage


class ContactPage(BasePage):
    CONTACT_US_BUTTON = (By.XPATH, f"// * [text() = 'Contact us']")
    NAME_FIELD = (By.ID, "cf-1")
    SUBJECT_FIELD = (By.ID, "cf-4")
    YOUR_MESSAGE_FIELD = (By.ID, "cf-5")
    EMAIL_FIELD = (By.ID, "cf-2")
    SEND_BUTTON = (By.CSS_SELECTOR, "input[class='wpcf7-form-control has-spinner wpcf7-submit btn-cf-submit']")
    EMAIL_MESSAGE = (By.XPATH, "//span[@class='wpcf7-not-valid-tip']")

    def contact_button(self):
        contact_us_button = self.driver.find_element(*self.CONTACT_US_BUTTON)
        contact_us_button.click()

    def set_name(self, name):
        name_field = self.driver.find_element(*self.NAME_FIELD)
        name_field.send_keys(name)

    def set_subject(self, subject):
        subject_field = self.driver.find_element(*self.SUBJECT_FIELD)
        subject_field.send_keys(subject)

    def set_message(self, message):
        your_message_field = self.driver.find_element(*self.YOUR_MESSAGE_FIELD)
        your_message_field.send_keys(message)

    def set_mail(self, email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

    def send_button(self):
        send_button = self.driver.find_element(*self.SEND_BUTTON)
        send_button.click()

    def email_message(self):
        return self.driver.find_element(*self.EMAIL_MESSAGE).text