from datetime import datetime, timedelta
import collections
import calendar


users = []


def init_data_load():
    Person = collections.namedtuple('Person', ['name', 'birthday'])
    users.append(Person('Jill', convert_datetime('17.05')))
    users.append(Person('Bob', convert_datetime('16.05')))
    users.append(Person('Bill', convert_datetime('18.05')))
    users.append(Person('Ann', convert_datetime('21.05')))
    users.append(Person('John', convert_datetime('22.05')))
    users.append(Person('Peter', convert_datetime('28.05')))
    return users


def get_today():
    return datetime.today()


def convert_datetime(str):
    return datetime.strptime(str, '%d.%m').replace(year=get_today().year)


def within_week_timeframe(date):
    today = get_today()
    saturday = today - timedelta(days=today.weekday()) + timedelta(days=5)
    friday = saturday + timedelta(days=6)
    if date >= saturday and date <= friday:
        return True
    else:
        return False


def main():
    users = init_data_load()
    congratulate(users)


def congratulate(users):
    results = collections.defaultdict(list)
    weekdays = list(calendar.day_name)
    for p in users:
        if within_week_timeframe(p.birthday):
            if p.birthday.weekday() == 5 or p.birthday.weekday() == 6:
                results[weekdays[0]].append(p.name)
            else:
                results[weekdays[p.birthday.weekday()]].append(p.name)
    print(dict(results))
    
    


if __name__ == '__main__':
    main()
