from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
# After you write the key in the file once, comment out the function

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter the Master Password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("Username:", user, "\n" + "Password:", passwd)

def add():
    name = input("Account Name: ")
    pwd = input("Account Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n") 

while True:
    mode = input("Would you like to Add a new password or View an existing password (add/view), or type in q to quit?: ")
    if mode == "q":
        break
    
    elif mode == "view":
        view()
        
    elif mode == "add": 
        add()
        
    else:
        print("Invalid mode. Please try again.")
        continue
print("End")