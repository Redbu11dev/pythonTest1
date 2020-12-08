import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        for i in range(10):
            if wd.find_element(By.NAME, "LoginForm"):
                break
            time.sleep(1)
        else:
            wd.fail(self, "time out")

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
