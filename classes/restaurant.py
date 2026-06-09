class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name.title() + " and has a very " +
        "tasty " + self.cuisine_type + " cuisine")


my_restaurant = Restaurant("Loom", "Vegan")
my_restaurant_two = Restaurant("Chiqui", "Mexican")
my_restaurant_three = Restaurant("Lotus", "Japanese")
my_restaurant.describe_restaurant()
my_restaurant_two.describe_restaurant()
my_restaurant_three.describe_restaurant()
