# type checking/avoiding cyclic imports solution - https://stackoverflow.com/a/39757388
from __future__ import annotations

from time import sleep
from typing import TYPE_CHECKING

from addressbook_tester.src.models.contact import Contact

if TYPE_CHECKING:
    from addressbook_tester.src.application import Application

from selenium.webdriver.support.ui import Select
import re


class ContactHelper:
    def __init__(self, app: Application):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        # click "submit"
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

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
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # self.select_contact_by_index(index)
        # wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         sleep(2)
    #         self.app.open_home_page()
    #         self.contact_cache = []
    #         for i, element in enumerate(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']")):
    #             # last_name = element.find_element_by_xpath("//td[2]").text
    #             # first_name = element.find_element_by_xpath("//td[3]").text
    #             xpath1 = f"//table[@id='maintable']/tbody/tr[{i+2}]/td[2]"
    #             xpath2 = f"//table[@id='maintable']/tbody/tr[{i+2}]/td[3]"
    #             last_name = element.find_element_by_xpath(xpath1).text
    #             first_name = element.find_element_by_xpath(xpath2).text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.contact_cache.append(Contact(last_name=last_name, first_name=first_name, id=id))
    #         # aa = len(self.contact_cache)
    #         # a = self.contact_cache
    #     return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            # sleep(2)
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(last_name=lastname, first_name=firstname, id=id,
                                                  all_phones_from_homepage =all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, home_phone_number=homephone,
                       mobile_phone_number=mobilephone, work_phone_number=workphone, phone_2=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone_number=homephone,
                       mobile_phone_number=mobilephone, work_phone_number=workphone, phone_2=secondaryphone)
