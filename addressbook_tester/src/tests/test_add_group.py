from addressbook_tester.src.models.group import Group


def test_add_group(app):
    app.group.create(Group("group1", "group1_header", "group1_footer"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
