from addressbook_tester.src.models.group import Group


def test_del_group(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
