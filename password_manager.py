master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Account Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n") 

while True:
    mode = input("Would you like to add a new password or view an existing password (add/view), or q to quit?: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add": 
        add()
    else:
        print("Invalid mode.")
        continue