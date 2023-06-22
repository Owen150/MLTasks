master_pwd = input("Enter the Master Password: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    pwd = input("Account Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n") 

while True:
    mode = input("Would you like to Add a new password or View an existing password (add/view), or type in q to quit?: ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add": 
        add()
    else:
        print("Invalid mode.")
        continue
print("End")