from random import randrange

from addressbook_tester.src.models.group import Group


def test_modify_group_name(app):
    if app.group.count() < 1:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     # if app.group.count() < 1:
#     #     app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New Header"))
#     new_groups = app.group.get_group_list()
#     assert len(new_groups) == len(old_groups)
