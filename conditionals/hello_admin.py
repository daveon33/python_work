usernames = ["admin", "david3", "bananini", "newuser1", "olduser1"]

for username in usernames:
    if(username == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Welcome back {username}, thank you for logging in again!")

    