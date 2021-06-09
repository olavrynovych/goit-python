from collections import UserDict, UserList
from datetime import datetime
import re


class AddresBook(UserList):
    def __init__(self):
        self.start_point = 0

    def add_record(self, record):
        self.data.append(record)

    def iterator(self, n):
        if self.start_point < len(self.data):
            before_index = self.start_point
            self.start_point = self.start_point + 1 + n
            return self.data[before_index:self.start_point]
        raise StopIteration
    # AddressBook реализует метод iterator, которые возвращает генератор по записям AddressBook и за одну итерацию возвращает представление для N записей.


class Field():
    def __init__(self, value=None):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        self.__value = new_val


class Record(Field, UserDict):
    # Record хранит объект Name в отдельном атрибуте.  ????
    Name = ''
    Birthday = ''

    def add_phone(self, phone):
        phones = self.data.get('phones', [])
        phones.append(phone)
        self.data['phones'] = phones

    def delete_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass

    def set_name(self, name):
        self.data.get('name', Name())

    def days_to_birthday(self):
        if not Birthday == None:
            date = datetime.strptime(Birthday.value, '%d-%m')
            today = datetime.now()
            date = date.replace(year=today.year)
            if today < date:
                return (date - today).days
            else:
                return (date.replace(year=date.year+1) - today).days


class Birthday():
    def __init__(self, value=None):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, date):
        date = str(date)
        pattern = r"(10|20|[0-2][1-9]|3[01])-(0[1-9]|1[0-2])"
        if re.search(pattern, date):
            self.__value = date
            print('Value is set: ' + date)
        else:
            print('Invalid date: ' + date)

    # def days_to_birthday(self):
    #     if not self.__value == None:
    #         date = datetime.strptime(self.__value, '%d-%m')
    #         today = datetime.now()
    #         date = date.replace(year=today.year)
    #         if today < date:
    #             return (date - today).days
    #         else:
    #             return (date.replace(year=date.year+1) - today).days


class Name(Field):
    name = ''


class Phone(Field):
    def __init__(self, value=None):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        phone = str(phone)
        pattern = r"[\d]{3}-[\d]{3}-[\d]{4}"
        if re.search(pattern, phone):
            self.__value = phone
            print('Value is set: ' + phone)
        else:
            print('Invalid phone number: ' + phone)
