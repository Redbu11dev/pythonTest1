from addressbook_tester.src.models.group import Group


def test_modify_group_name(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_group_header(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New Header"))
