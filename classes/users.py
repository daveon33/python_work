class User():
    def __init__(self, first_name, last_name, email, phone, id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.id_num = id_num

    def describe_user(self):
        print("The user(id =  " + self.id_num + ") with name "  + self.first_name + " " + self.last_name + " has as email " +
        self.email + " and  phone number " + self.phone)
    
    def greet_user(self):
        print("Hello " + self.first_name + " let's keep pushing!!!")


user_one = User("David", "Gonzalez", "anyemail@not.com", "0012248", "000001")
user_one.describe_user()
user_one.greet_user()