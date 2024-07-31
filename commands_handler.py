from errors_handler import input_error
from functionality import AddressBook, Record


# add new contact to the dictionary
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


# change phone for existed contact
# @input_error
# def change_contact(args, contacts):
#     name, phone = args
#     if name in contacts:
#         contacts[name] = phone
#         return "Contact updated"
#     else:
#         return "Contact not found"


# show phone of existed contact
@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        message = f"{record.name}: {"; ".join(p.value for p in record.phones)}"
    else:
        message = "Contact not found"
    return message


# show all contacts from the dictionary
def show_all(book: AddressBook):
    if not book:
        return "No contacts found."
    else:
        contacts = [str(value) for key, value in book.items()]
        return "\n".join(contacts)
