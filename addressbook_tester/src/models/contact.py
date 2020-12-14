from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, photo_path=None, title=None,
                 company=None, address=None, home_phone_number=None, mobile_phone_number=None, work_phone_number=None,
                 fax_number=None, email_1=None, email_2=None, email_3=None, homepage=None, birthday_day=None,
                 birthday_month=None, birthday_year=None, anniversary_day=None, anniversary_month=None,
                 anniversary_year=None, group_name=None, address_2=None, phone_2=None, notes=None, id=None,
                 all_phones_from_homepage = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo_path = photo_path
        self.title = title
        self.company = company
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax_number = fax_number
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group_name = group_name
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return f"{self.id}:{self.last_name}:{self.first_name}"

    def __eq__(self, o) -> bool:
        return (self.id is None or o.id is None or self.id == o.id) and self.last_name == o.last_name \
               and self.first_name == o.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
