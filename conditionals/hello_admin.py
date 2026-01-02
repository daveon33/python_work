usernames = ["admin", "david3", "bananini", "newuser1", "olduser1"]

for username in usernames:
    if(username == 'admin'):
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Welcome back {username}, thank you for logging in again!")

usernames = []

if usernames:
    for username in usernames:
        if(username == 'admin'):
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Welcome back {username}, thank you for logging in again!")

else:
    print("We need to find some users!")