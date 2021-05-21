from collections import UserDict, UserList


class AddresBook(UserList):
    def add_record(self, record):
        self.data.append(record)


class Field():
    pass


class Record(Field, UserDict):
    # Record хранит объект Name в отдельном атрибуте.  ????
    Name = ''

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


class Name(Field):
    name = ''


class Phone(Field):
    pass
