# type checking/avoiding cyclic imports solution - https://stackoverflow.com/a/39757388
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from addressbook_tester.src.application import Application

import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app: Application):
        self.app = app

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        for i in range(10):
            if wd.find_element(By.NAME, "LoginForm"):
                break
            time.sleep(1)
        else:
            wd.fail(self, "time out")

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

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
