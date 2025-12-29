favorite_pizzas = ['pineapple', 'mexican', 'Chicken and mushrooms']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('paisa')
friend_pizzas.append('pepperoni')

for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!")
print(f"My favorite pizzas are: {favorite_pizzas}")

for pizza in friend_pizzas:
    print(pizza)