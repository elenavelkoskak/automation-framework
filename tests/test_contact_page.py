import unittest
from selenium import webdriver
from automationframework.pages.ContactPage import ContactPage
from automationframework.config.config import *
from automationframework.data.emails import emails


class TestContactPage(unittest.TestCase):
    name = "name1"
    subject = "subject1"
    message = "message1"

    def setUp(self) -> None:
        if BROWSER == "chrome":
            self.driver = webdriver.Chrome()
        elif BROWSER == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.get(BASEURL)
        self.contact_page = ContactPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email_message_1(self):
        self.driver.execute_script("window.scrollTo(0,800)")
        self.contact_page.contact_button()
        self.contact_page.set_name(self.name)
        self.contact_page.set_subject(self.subject)
        self.contact_page.set_message(self.message)
        self.contact_page.set_mail(emails[0])
        self.contact_page.send_button()
        if self.contact_page.email_message() == "The e-mail address entered is invalid.":
            assert True
        else:
            assert False

    def test_wrong_email_message_2(self):
        self.driver.execute_script("window.scrollTo(0,800)")
        self.contact_page.contact_button()
        self.contact_page.set_name(self.name)
        self.contact_page.set_subject(self.subject)
        self.contact_page.set_message(self.message)
        self.contact_page.set_mail(emails[1])
        self.contact_page.send_button()
        if self.contact_page.email_message() == "The e-mail address entered is invalid.":
            assert True
        else:
            assert False

    def test_wrong_email_message_3(self):
        self.driver.execute_script("window.scrollTo(0,800)")
        self.contact_page.contact_button()
        self.contact_page.set_name(self.name)
        self.contact_page.set_subject(self.subject)
        self.contact_page.set_message(self.message)
        self.contact_page.set_mail(emails[2])
        self.contact_page.send_button()
        if self.contact_page.email_message() == "The e-mail address entered is invalid.":
            assert True
        else:
            assert False

    def test_wrong_email_message_4(self):
        self.driver.execute_script("window.scrollTo(0,800)")
        self.contact_page.contact_button()
        self.contact_page.set_name(self.name)
        self.contact_page.set_subject(self.subject)
        self.contact_page.set_message(self.message)
        self.contact_page.set_mail(emails[3])
        self.contact_page.send_button()
        if self.contact_page.email_message() == "The e-mail address entered is invalid.":
            assert True
        else:
            assert False

    def test_wrong_email_message_5(self):
        self.driver.execute_script("window.scrollTo(0,800)")
        self.contact_page.contact_button()
        self.contact_page.set_name(self.name)
        self.contact_page.set_subject(self.subject)
        self.contact_page.set_message(self.message)
        self.contact_page.set_mail(emails[4])
        self.contact_page.send_button()
        if self.contact_page.email_message() == "The e-mail address entered is invalid.":
            assert True
        else:
            assert False
