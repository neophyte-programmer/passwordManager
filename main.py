# This program organises and stores your passwords however,
# it is a beginner attempt so don't store your actual passwords in it
masterPassword = input("What is the master password? ")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User:", user, "| Password:", passwd)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")

"""
    1. Using the with keyword allows for the file to automatically close after using it
    2. The 'a' mode makes the file appendable a.k.a, it allows for more info to be added at the end of the file and in
    in this case, it is necessary so that the user can add more passwords. And if the specified file does not exist,
    it creates a new one
    the other modes - 'r' is for read only and 'w' is for writing and if the file already exists, it will overwrite it
    3. The open keyword just opens the specified file in the specified mode
    4. rstrip (in this case) removes a carriage return (\n from add() function) from the line
"""

while True:
    mode = input("Would you like to add a new password or view existing passwords? (add, view) "
                 "Press 'q' to quit. ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter a valid option.")
        continue
