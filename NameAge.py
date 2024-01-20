def gather_user_info():
    """Prompts the user for their name and age."""
    firstName = input("What's your first name? ")
    lastName = input("What's your last name? ")
    age = int(input("How old are you? "))
    return firstName, lastName, age

def print_welcome_message(name, birthYear):
    """Prints a personalized welcome message."""
    print(f"""
******************
Welcome, {name}!
You were born in {birthYear}.
******************
""")
firstName, lastName, age = gather_user_info()
birthYear = 2024 - age
print_welcome_message(f"{firstName} {lastName}", birthYear)
