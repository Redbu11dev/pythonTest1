import pytest

from addressbook_tester.src.application import Application
from addressbook_tester.src.models.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("group1", "group1_header", "group1_footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
