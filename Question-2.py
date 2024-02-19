"""2)Write a program to check the validity of a password. Primary conditions for password validation:
- minimum 8 charecters
- The alphabet must be between [a-z]
- At least one alphabet should be of Upper Case [A-Z]
- At least 1 number or digit between [0-9].
- At least 1 character from [ _ or @ or $ ]."""


user_database = {}

# Registration form
def registration_form():
    print("Welcome to the Our Team")
    username = input("Enter a username: ")
    email = input("Enter your email address: ")
    print(""" conditions for password validation:
         - minimum 8 characters.
         - The alphabet must be between [a-z].
         - At least one alphabet should be of Upper Case [A-Z].
         - At least 1 number or digit between [0-9].
         - At least 1 character from [ _ or @ or $ ].)""")
    password = input("Enter a password: ")

    register(username, password, email)

def register(username, password, email):
    if username in user_database:
        print("Username already exists. Please choose a different username.")
    elif password_validation(password):
        user_database[username] = {'password': password, 'email': email}
        print("Registration successful. You can now log in.")
    else:
        print("Invalid password. Please check the password criteria.")


def login():
    print("\nEnter your username and password to login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database and user_database[username]['password'] == password:
        print(f"Welcome, {username}! Login successful.")
    else:
        print("Login failed. Please check your username and password.")

def password_validation(password):
    symbols = ['$', '@', '_']
    if len(password) < 8:
        print("Password must contain minimum 8 characters.")
    elif not any(char.islower() for char in password):
        print("The password should have alphabet between [a-z].")
    elif not any(char.isdigit() for char in password):
        print("The password should have at least one number.")
    elif not any(char.isupper() for char in password):
        print("The password should have at least one capital letter.")
    elif not any(char in symbols for char in password):
        print("The password should have at least one of the symbols $,@,_")
    else:
        print("Password meets all criteria. Registration successful!.")
        return True
    return False

while True:
    print("\n 1. Signup\n 2. Login\n 3. Exit")
    choice = input("Enter your choice (1/2/3): ")


    if choice == '1':
        registration_form()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

