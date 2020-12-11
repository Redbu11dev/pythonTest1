from random import randrange

from addressbook_tester.src.models.contact import Contact


def test_modify_contact_last_name(app):
    app.contact.contact_cache = None
    if app.contact.count() < 1:
        app.contact.create(Contact(last_name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact1 = Contact(last_name=f"New Last Name{randrange(9999)}", first_name=f"New First Name {randrange(9999)}")
    contact1.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact1)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    # old_contacts[index] = contact1
    for i, c in enumerate(old_contacts):
        if c.id == contact1.id:
            old_contacts[i] = contact1
    #         break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_nickname(app):
#     if app.contact.count() < 1:
#         app.contact.create(Contact(last_name="test"))
#     app.contact.modify_first_contact(Contact(nickname="New Nickname"))
