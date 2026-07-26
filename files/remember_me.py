from pathlib import Path
import json


def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("What is your age? ")
    favorite_language = input("What is your favorite programming language? ")
    my_user = {
        'username': username,
        'age': age,
        'favorite language': favorite_language,
    }
    contents = json.dumps(my_user)
    path.write_text(contents)
    return my_user

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    my_user = get_stored_user(path)
    if my_user:
        print(f"Welcome back, {my_user["username"]}. Your age is my_user["age"]}, and your favorite programming language is {my_user["favorite language"]}!")
    else:
        my_user = get_new_user(path)
        print(f"We'll remember you when you come back, {my_user['username']}!")

greet_user()