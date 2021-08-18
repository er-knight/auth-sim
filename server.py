import sqlite3

from client import client

class server:

    def __init__(self):
        connection = sqlite3.connect("user.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)""")

    def login(self, user):
        connection = sqlite3.connect("user.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""SELECT * FROM users WHERE username=?""", (user.username, ))
            result = db_cursor.fetchone()

        if result:
            password = result[1]
            if password == user.password:
                return "Logged in successfully"
            else:
                return "Incorrect password"
              
        return "User not found"

    def signup(self, user):
        connection = sqlite3.connect("user.db") 

        db_cursor = connection.cursor()
        db_cursor.execute("""SELECT * FROM users WHERE username=?""", (user.username, ))
        result = db_cursor.fetchone()

        if result:
            return "User already exists"

        db_cursor.execute("""INSERT INTO users VALUES (?, ?)""", (user.username, user.password))
        connection.close()

        return "Signed up successfully"

if __name__ == "__main__":

    username = "username"
    password = "password"

    user = client(username, password)
    
    assert server().login(user) == "User not found"
    