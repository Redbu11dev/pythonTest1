import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_viewpage(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone_number == contact_from_edit_page.home_phone_number
    assert contact_from_view_page.work_phone_number == contact_from_edit_page.work_phone_number
    assert contact_from_view_page.mobile_phone_number == contact_from_edit_page.mobile_phone_number
    assert contact_from_view_page.phone_2 == contact_from_edit_page.phone_2

def test_all_info_on_home_page(app):
    all_homepage_contacts = app.contact.get_contact_list()
    random_index = randrange(len(all_homepage_contacts))
    contact_from_home_page = all_homepage_contacts[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.email_1, contact.email_2,
                                                          contact.email_3]))))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.home_phone_number, contact.mobile_phone_number,
                                                          contact.work_phone_number, contact.phone_2]))))
