import mysql.connector

from addressbook_tester.src.models.contact import Contact
from addressbook_tester.src.models.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connecton = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                 autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connecton.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connecton.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connecton.close()
