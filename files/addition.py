number_one = input('What\'s the first number? ')
number_two = input('What\'s the second number? ')

try:
    addition = int(number_one) + int(number_two)
except ValueError:
    print("At least one of the inputs was not a number, try again")
else:
    print(f"The sum is {addition}")