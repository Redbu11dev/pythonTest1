# type checking/avoiding cyclic imports solution - https://stackoverflow.com/a/39757388
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from addressbook_tester.src.application import Application

from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app: Application):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        # click "submit"
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value(contact.first_name, "firstname")
        self.change_field_value(contact.middle_name, "middlename")
        self.change_field_value(contact.last_name, "lastname")
        self.change_field_value(contact.nickname, "nickname")
        if contact.photo_path:
            wd.find_element_by_name("photo").send_keys(contact.photo_path)
        self.change_field_value(contact.title, "title")
        self.change_field_value(contact.company, "company")
        self.change_field_value(contact.address, "address")
        self.change_field_value(contact.home_phone_number, "home")
        self.change_field_value(contact.mobile_phone_number, "mobile")
        self.change_field_value(contact.work_phone_number, "work")
        self.change_field_value(contact.fax_number, "fax")
        self.change_field_value(contact.email_1, "email")
        self.change_field_value(contact.email_2, "email2")
        self.change_field_value(contact.email_3, "email3")
        self.change_field_value(contact.homepage, "homepage")
        self.change_selector_value(contact.birthday_day, "bday")
        self.change_selector_value(contact.birthday_month, "bmonth")
        self.change_field_value(contact.birthday_year, "byear")
        self.change_selector_value(contact.anniversary_day, "aday")
        self.change_selector_value(contact.anniversary_month, "amonth")
        self.change_field_value(contact.anniversary_year, "ayear")
        self.change_selector_value(contact.group_name, "new_group")
        self.change_field_value(contact.address_2, "address2")
        self.change_field_value(contact.phone_2, "phone2")
        self.change_field_value(contact.notes, "notes")

    def change_selector_value(self, value, field_name):
        wd = self.app.wd
        if value:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_contacts_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home").click()

    def verify_account_created(self, contact):
        wd = self.app.wd
        # check if contact is in the table
        table_elements = wd.find_elements_by_xpath(
            f"//table[@id='maintable']/tbody/tr/td[contains(text(),'{contact.last_name}')]")
        assert len(table_elements) > 0
        # for element in table_elements:
        #     print(f"{element.text}\n")

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
