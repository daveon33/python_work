current_users = ["admin", "david3", "bananini", "newuser1", "olduser1"]
new_users = ["david3", "hello2", "newuser1", "newhere", "mariana2"]

for user in new_users:
    if user.lower() in current_users:
        print("This username is already taken! please choose another one...")
    else:
        print("Congratulations! This username is free to be used!")

