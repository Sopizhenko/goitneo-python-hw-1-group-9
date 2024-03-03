def parse_input(user_input):
	cmd, *args = user_input.split()
	cmd = cmd.strip().lower()
	return cmd, *args


def add_contact(args, contacts):
	name, phone = args
	contacts[name] = phone
	return "Contact added."


def change_contact(args, contacts):
	name, phone = args
	if name in contacts:
		contacts[name] = phone
		return "Contact updated."
	else:
		return "Contact not found."


def get_contact(args, contacts):
	name = args[0]
	if name in contacts:
		return f"The phone number of {name} is {contacts[name]}."
	else:
		return "Contact not found."


def get_all_contacts(contacts):
	if contacts:
		return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
	else:
		return "The contact list is empty."


def help():
	return """Available commands:
	- hello: Show a welcome message.
	- add [name] [phone]: Add a new contact.
	- change [name] [phone]: Update a contact.
	- phone [name]: Get the phone number of a contact.
	- all: Get all contacts.
	- help: Show this help message.
	- close: Close the program.
	- exit: Close the program."""


def main():
	contacts = {}
	print("Welcome to the assistant bot!")
	while True:
		command = input("Enter a command: ")
		command, *args = parse_input(command)

		if command in ["close", "exit"]:
			print("Goodbye!")
			break
		elif command == "add":
			print(add_contact(args, contacts))
		elif command == "change":
			print(change_contact(args, contacts))
		elif command == "phone":
			print(get_contact(args, contacts))
		elif command == "all":
			print(get_all_contacts(contacts))
		elif command == "help":
			print(help())
		elif command == "hello":
			print("How can I help you?")
		else:
			print("Invalid command.")


if __name__ == "__main__":
	main()