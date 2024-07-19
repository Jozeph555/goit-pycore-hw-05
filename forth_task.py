"""Forth task - Helper Console Bot"""


def parse_input(user_input):
    """Parses the command entered by the user 
    into a command and its arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_value_error(func):
    """
    Decorator function that handles ValueError
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner


def input_key_index_error(func):
    """
    Decorator function that handles KeyError 
    and IndexError 
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such name in contacts."
        except IndexError:
            return "Give me name please"
    return inner


@ input_value_error
def add_contact(args, contacts):
    """Adds a new contact to the 
    contact dictionary"""
    name, phone = args
    if name in contacts:
        return "The name is already in contacts.\n" +\
               "If you'd like to change contact,\n" +\
               "please use 'change' command"
    contacts[name] = phone
    return "Contact added."


@ input_value_error
def change_contact(args, contacts):
    """Changes an existing contact 
    in the contact dictionary"""
    name, phone = args
    if name not in contacts:
        return "There is no such name in contacts"
    contacts[name] = phone
    return "Contact changed."


@ input_key_index_error
def show_phone(name, contacts):
    """Outputs the phone number 
    for the specified contact"""
    name = name[0]
    return contacts[name]


def show_all(contacts):
    """Outputs all saved contacts 
    with phone numbers"""
    return contacts


def main():
    """Main function"""

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            all_contacts = show_all(contacts)
            for name, phone in all_contacts.items():
                print(f"{name}: {phone}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
