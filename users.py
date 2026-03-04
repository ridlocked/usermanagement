import getpass
import json



# imports getpass which allows for terminal output to hide the users inputs

## not implemented,
# goal:
# user creation, password and user storage, matching pass to user key:value
# password creation, checked against password strength tester, stored
# login with authenticated users, keeping users:pass stored, allowing for login later
# data file for those stored, hashed, salted
# use hashes to confirm login not plain text
##


def user_load():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
users = user_load()

def user_menu():
    print("Menu Options")
    print("1. Login")
    print("2. Create User")
    print("3. Forgot Password")
    print("4. Exit")

    selected_option = input("Please select an option from the menu:\n")

    if selected_option in ["1", "login"]:
        login()

    elif selected_option in ["2", "create user"]:
        user_creation()

    elif selected_option in ["3", "forgot password"]:
        forgot_password()

    elif selected_option in ["4", "exit"]:
        exit()

    else:
        restart_menu = input("Invalid Option Selected, try again? (yes/no):\n")

        if restart_menu in ["yes", "y"]:
            user_menu()

        elif restart_menu in ["no", "n"]:
            exit()
def logged_in_user_menu_tld():
    print("1. Productivity")
    print("2. Account Settings")
    print("3. Logout")
def productivity_menu():
    print("Productivity Menu")
def account_menu():
    print("Account Menu")
    print("1. Change Password")
    print("2. Change Username")
    print("3. Delete Account")

def login():
    password_attempts = 0 # sets counter to 0 at the start of this function every time
    login_accepted = False # states a default state of False till other checks have been completed

    while password_attempts < 3: # while loop, while the variable before stays below 3, the below function will run
        username = input("Please enter your username:\n")
        password = getpass.getpass("Please enter your password:\n")

        if username in users and users[username] == password:
            login_accepted = True # if the condition above is met and both the username and password match,
            # a record on the system, the value of login_accepted gets changed to True
            print("User " + username + " logged in")
            # provides information to the user confirming that they have been logged in
            user_home(username)
            # calls the user_home function and passes along the variable username for welcoming banner
            return login_accepted
            # returns the login_accepted value to the function to reflect the conditions being met or unmet

        else:
            password_attempts += 1
            # if the conditions are not met, increase the passwords_attempts counter by 1, ever more ensuring,
            # that the previous system actually works and if the counter reaches 3 the login will be aborted.
            print("Invalid username or password.")

            if password_attempts < 3:
                # checks to see if the counter is less than 3 before printing the next statement
                print("Please try again.\nAttempts Remaining:", 3 - password_attempts)
                # adds a value of one to the counter while attempts are being made


    return login_accepted
    # after each counter increase of the else portion of the function, return the value of login_accepted to what called
    # the login function, and run through it again till the counter has either been reached or the user has been logged in



def user_home(username):
    # user home function, ideally some form of dashboard for the user, perhaps change password, make a note
    # runs with the passed variable username so the next print line welcomes the user who passes the login stage
    print("Welcome back, " + username + "!")

    logged_in_user_menu_tld()
    selected_option = input("What would you like to do today?\n")
    if selected_option in ["1", "Productivity"]:
        productivity_menu()
    if selected_option in ["2", "Account Settings"]:
        account_menu()
    if selected_option in ["3", "Logout"]:
        login()
    else:
        exit()




def user_creation():
    username = input("Please enter your desired username:\n")

    if username in users:
        print("Username Taken, try again.")
        user_creation()


    while True:  # infinite loop glitch x, nah it just keeps running the below code till
        # either it is shot in the head or it gets what it wants
        password = getpass.getpass("Enter a password:\n")
        # prompts the user for a password to create their account,
        # uses the getpass function to hide the users input when typing

        if password_strength(password):
            # condition checking
            # passes the password variable to the password_strength function to check that it meets the requirements

            users[username] = password
            save_user(users)
            # opens the created dictionary at the top of the script, appends the password that passed the check
            # to the stored username variable from earlier, creating a pair

            print("User created successfully.")
            # confirms to the user that the option was successful

            menu_choice = input("Return to main menu? (yes/no):\n")

            if menu_choice in ["yes", "y"]:
                user_menu()
            elif menu_choice in ["no", "n"]:
                exit()

            break
            # dies, simply passes away

        else:
            print("Please try again.\n")

def save_user(inside_users):
    with open("users.json", "w") as file:
        json.dump(inside_users, file)

def forgot_password():
    print() # placeholder



def change_password():
    print()


def password_strength(entered_password):
    accepted = True
    # default accepted state, set to True as nothing has been checked yet

    special_chars = ('!', '£', '%', '^', '&', '*', '(', ')', '_', '+', '@', '#', '"')
    # creates an immutable container, tuple, for the special characters required in the password

    if len(entered_password) < 8:
        print("This password does not meet the required character count")
        accepted = False
        # checks to see if the input meets the min char count requirement
        # if it doesn't, flip the accepted condition to False

    if ' ' in entered_password:
        print("invalid character in password, please try again")
        accepted = False
        # checks to see if the input contains a space,
        # if it does, flip the accepted condition to False

    special_char_present = False
    upper_char_present = False
    # same as before but sets the value to false until the requirement is met

    for char in entered_password:
        if char in special_chars:
            # runs each character against the special_chars tuple and checks to see if the requirement has been met
            special_char_present = True
            # swaps the boolean value for special_char_present to True once the requirement is met

        if char.isupper():
            upper_char_present = True

        if special_char_present and upper_char_present:
            break

            # once both conditions are met, special char and upper case, the loop stops
            # doesn't check the rest of the chars

    if not upper_char_present:
        print("password must contain at-least one uppercase letter")
        accepted = False

    if not special_char_present:
        print("Password must contain at least one special character")
        accepted = False

    if accepted:
        print("password accepted")
    return  accepted


user_menu()