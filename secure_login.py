import hashlib

users = {}

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users[username] = hashed_password
    print("Registration Successful!")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid Username or Password")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
