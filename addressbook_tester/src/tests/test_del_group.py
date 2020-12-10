from addressbook_tester.src.models.group import Group


def test_del_group(app):
    app.group.delete_first_group()
