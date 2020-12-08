from selenium import webdriver

from addressbook_tester.src.helpers.contact_helper import ContactHelper
from addressbook_tester.src.helpers.group_helper import GroupHelper
from addressbook_tester.src.helpers.session_helper import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


