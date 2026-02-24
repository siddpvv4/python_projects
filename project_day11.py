import random
import string
import os
import getpass

DATA_FILE = "passwords.txt"
MASTER_FILE = "master.txt"

# ---------------- MASTER PASSWORD SETUP ----------------

def setup_master():
    if not os.path.exists(MASTER_FILE):
        print("=== FIRST TIME SETUP ===")
        master = getpass.getpass("Create a MASTER password: ")
        confirm = getpass.getpass("Confirm MASTER password: ")

        if master == confirm:
            with open(MASTER_FILE, "w") as f:
                f.write(master)
            print("Master password created successfully!\n")
        else:
            print("Passwords did not match. Restart program.")
            exit()


def login():
    with open(MASTER_FILE, "r") as f:
        saved = f.read()

    for attempt in range(3):
        entered = getpass.getpass("Enter MASTER password: ")
        if entered == saved:
            print("Login successful!\n")
            return
        else:
            print("Wrong password!")

    print("Too many failed attempts. Exiting.")
    exit()


# ---------------- PASSWORD GENERATOR ----------------

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# ---------------- SAVE PASSWORD ----------------

def save_password():
    website = input("Website/App: ")
    username = input("Username/Email: ")

    choice = input("Auto-generate password? (y/n): ")

    if choice.lower() == 'y':
        password = generate_password()
        print("Generated password:", password)
    else:
        password = getpass.getpass("Enter password: ")

    with open(DATA_FILE, "a") as f:
        f.write(f"{website} | {username} | {password}\n")

    print("Password saved successfully!\n")

# ---------------- VIEW PASSWORDS ----------------

def view_passwords():
    if not os.path.exists(DATA_FILE):
        print("No saved passwords yet.\n")
        return

    print("\n--- STORED ACCOUNTS ---")
    with open(DATA_FILE, "r") as f:
        for line in f:
            print(line.strip())
    print()


# ---------------- SEARCH PASSWORD ----------------

def search_password():
    site = input("Enter website to search: ")

    if not os.path.exists(DATA_FILE):
        print("No saved passwords.\n")
        return

    found = False
    with open(DATA_FILE, "r") as f:
        for line in f:
            if site.lower() in line.lower():
                print("Found:", line.strip())
                found = True

    if not found:
        print("No matching account found.\n")


# ---------------- MENU ----------------

def menu():
    while True:
        print("====== PASSWORD MANAGER ======")
        print("1. Save Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Generate Random Password")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("Strong Password:", generate_password(), "\n")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option\n")


# ---------------- MAIN ----------------

setup_master()
login()
menu()
