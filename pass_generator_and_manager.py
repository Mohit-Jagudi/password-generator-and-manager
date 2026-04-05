import random
import string
import os

FILE_NAME = "passwords.txt"

# pass generator
def generate_password(length, characters):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password


# save pass
def save_password(app, password):
    data = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if ":" in line:
                    saved_app, saved_pass = line.strip().split(":")
                    data[saved_app.lower()] = saved_pass

    data[app.lower()] = password

    with open(FILE_NAME, "w") as file:
        for key in data:
            file.write(key + ":" + data[key] + "\n")

    print("Password saved/updated successfully.")


# fetch 
def fetch_password(app):
    if not os.path.exists(FILE_NAME):
        print("No saved passwords found.")
        return

    app = app.lower()
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            if ":" in line:
                saved_app, saved_pass = line.strip().split(":")
                if saved_app.lower() == app:
                    print("Password for", app, ":", saved_pass)
                    found = True
                    break

    if not found:
        print("Password not found.")


# main
while True:
    try:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Check saved passwords")
        print("2. Generate new password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            app = input("Enter app name: ").strip()
            if app == "":
                print("App name cannot be empty.")
            else:
                fetch_password(app)

        elif choice == "2":

            try:
                length = int(input("Enter password length: "))
            except ValueError:
                print("Please enter a valid number for length.")
                continue

            if length < 8:
                print("Password must be at least 8 characters long.")
                continue

            print("\n1. Random Password")
            print("2. Custom Password")

            mode = input("Choose option (1/2): ").strip()

            if mode == "1":
                characters = string.ascii_letters + string.digits + string.punctuation

            elif mode == "2":
                characters = ""

                use_upper = input("Include A-Z? (y/n): ").strip()
                use_lower = input("Include a-z? (y/n): ").strip()
                use_digits = input("Include 0-9? (y/n): ").strip()
                use_symbols = input("Include symbols? (y/n): ").strip()

                if use_upper.lower() == "y":
                    characters += string.ascii_uppercase
                if use_lower.lower() == "y":
                    characters += string.ascii_lowercase
                if use_digits.lower() == "y":
                    characters += string.digits
                if use_symbols.lower() == "y":
                    characters += string.punctuation

                if characters == "":
                    print("No selection made. Using all characters by default.")
                    characters = string.ascii_letters + string.digits + string.punctuation

            else:
                print("Invalid choice. Using random password.")
                characters = string.ascii_letters + string.digits + string.punctuation

            password = generate_password(length, characters)
            print("Generated Password:", password)

            save = input("Do you want to save this password? (y/n): ").strip()

            if save.lower() == "y":
                app = input("Enter app name: ").strip()
                if app == "":
                    print("App name cannot be empty. Password not saved.")
                else:
                    save_password(app, password)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except Exception:
        print("Unexpected error occurred. Please try again.")
