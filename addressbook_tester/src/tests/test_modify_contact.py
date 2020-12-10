from addressbook_tester.src.models.contact import Contact


def test_modify_contact_last_name(app):
    app.contact.modify_first_contact(Contact(last_name="New Last Name"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="New Nickname"))
