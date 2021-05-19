def hello():
    print('How can I help you?')


def add(user):
    name, phone = user.split(' ')
    CONTACTS[name] = phone
    print(f'Contact \'{name}\' has been added.')


def change(user):
    name, phone = user.split(' ')
    CONTACTS[name] = phone
    print(f'Contact \'{name}\' has been changed')


def phone(name):
    print(f'{CONTACTS[name]}')


def show_all():
    print(CONTACTS)


def good_bye():
    print('Good bye!')


FUNCTIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show_all': show_all,
    'good_bye': good_bye,
    'close': good_bye,
    'exit': good_bye
}

CONTACTS = {}


def parser(str):
    user_input = str.split(' ')
    return user_input


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyError:
            print('Key error')
        except ValueError:
            print('Give me name and phone please')
        except IndexError:
            print('Index error')
        except NameError:
            print('Name error')
        else:
            return result
    return inner


def get_operation_handler(func_name):
    return FUNCTIONS[func_name]


@input_error
def main():
    print('How can I help you?')
    while True:
        user_input = input().lower()
        args = parser(user_input)
        func = get_operation_handler(args[0])
        if user_input == 'add' or user_input == 'change':
            user_info = input('Please enter name and phone')
            func(user_info)
        elif user_input == 'phone':
            name = input('Please enter name')
            func(name)
        else:
            func()


if __name__ == '__main__':
    main()


# def asd(*args, **kwargs):
#     if user_input == 'add' or user_input == 'change':
#         user_info = input('Please enter name and phone').split(' ')
#         get_operation_handler(user_input, user_info[0], user_info[1])
#     elif user_input == 'phone':
#         name = input('Please enter name')
#         get_operation_handler(user_input, name)
#     else:
#         get_operation_handler(user_input)
