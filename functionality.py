from collections import UserDict
from entities import Name, Phone, Birthday
from datetime import datetime, date, timedelta
from typing import Callable
from birthday_func import adjust_for_weekend, date_to_string


class Record:
    """
    Save contact info including name and phones
    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        return ValueError

    def remove_phone(self, phone_str: str):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_str:
                del self.phones[i]
                return
        return ValueError

    def find_phone(self, phone_str: str):
        for phone in self.phones:
            if phone.value == phone_str:
                return phone.value
        return None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday).value


class AddressBook(UserDict):
    """
    Save and manage records
    """

    def add_record(self, record):
        """
        Add record to self.data
        """
        self.data[record.name.value] = record
        return record

    def find(self, value: str):
        """
        Find record by name
        """
        return self.data.get(value, None)

    def delete(self, value: str):
        """
        Delete record by name
        """
        if value in self.data:
            del self.data[value]

    def get_upcoming_birthdays(self, days=7) -> list:
        upcoming_birthdays = []
        today = date.today()
        # users = []
        # for key, value in self.data.items():
        #     users.append({"name": str(value.name), "birthday": value.birthday})
        # print(users)

        for record in self.data.values():
            birthday_this_year = record.birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = record.birthday.replace(year=today.year + 1)
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append(
                {
                    "name": record.name.value,
                    "birthday": congratulation_date_str,
                }
            )

        return upcoming_birthdays


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("20.01.1992")
# print(john_record)
print(john_record.name)
print(john_record.birthday)


# Додавання запису John до адресної книги
book.add_record(john_record)
# # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("12.03.2000")
# print(jane_record)
book.add_record(jane_record)

# # Виведення всіх записів у книзі

# print(book)
# book.get_upcoming_birthdays(users)

# print(book.get_upcoming_birthdays())
for key, value in book.items():
    print(value)
