from hashlib import sha256

class client:

    def __init__(self, username, password):
        self.username = username
        self.password = sha256(password.encode()).hexdigest()

    
if __name__ == "__main__":
    
    username = "username"
    password = "password"

    assert sha256(password.encode()).hexdigest() == client(username, password).password
    