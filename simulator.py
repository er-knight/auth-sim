from hashlib import sha256
from client  import client
from server  import server
from time    import sleep

def clear_screen():
    import os 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def loading():
    symbols = ["--", "\\", "|", "/"]
    for i in (symbols * 5):
        print(i.center(15), end=" ", flush=True)
        sleep(0.5)
        clear_screen()
    print()

def login():
    username = input("Username\n→ ").strip()
    password = input("Password\n→ ").strip()

    password = sha256(password.encode()).hexdigest()

    user = client(username, password)

    clear_screen()
    loading()
    clear_screen()

    result = server().login(user)
    print(result)

def signup():
    username = input("Username\n→ ").strip()
    password = input("Password\n→ ").strip()

    password = sha256(password.encode()).hexdigest()

    user = client(username, password)

    clear_screen()
    loading()
    clear_screen()

    result = server().signup(user)
    print(result)
    
if __name__ == "__main__":

    clear_screen()

    print("Welcome to auth-sim!\n")
    option = input("[L]ogin or [S]ignup\n→ ").strip().upper()[0]

    if option == "L":
        login()
    else:
        signup()

# sample user
# username - johndoe
# password - johndoe123