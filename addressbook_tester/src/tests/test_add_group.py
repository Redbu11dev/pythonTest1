from addressbook_tester.src.models.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group("group1", "group1_header", "group1_footer")
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# app.session.logout()


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group("", "", "")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(new_groups) == len(old_groups) + 1
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
