from commands_handler import add_contact, show_phone, show_all
from parse_input import parse_input
from functionality import AddressBook


def main():
    record = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, record))
            case "change":
                print(add_contact(args, record))
            case "phone":
                print(show_phone(args, record))
            case "all":
                print(show_all(record))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()