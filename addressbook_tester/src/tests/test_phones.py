

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_phone_number == contact_from_edit_page.home_phone_number
    assert contact_from_home_page.work_phone_number == contact_from_edit_page.work_phone_number
    assert contact_from_home_page.mobile_phone_number == contact_from_edit_page.mobile_phone_number
    assert contact_from_home_page.phone_2 == contact_from_edit_page.phone_2