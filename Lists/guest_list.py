guest_list = ['Dante', 'Reno', 'Tito']

print(f"I would love to see you all at my party this weekend. Can't wait to see {guest_list[0]}'s dance moves, laugh with the goofy {guest_list[1]}, and enjoy a pleasant conversation with {guest_list[2]}")

print(f"It seems only {guest_list[1]} is unable to attend my party")

guest_list[1] = 'Andres'

print(f"Now {guest_list[1]} is invited and he will bring some refreshments for all!")

print("I have found a bigger table! Now I can invite 3 more people...")

guest_list.insert(0, 'Giovanni')
guest_list.insert(2, 'Mateo')
guest_list.append('Daniel')

print(f"I hope you can come to my party {guest_list[0]}, {guest_list[2]} and {guest_list[-1]}")

print("Unfortunately there's a change in plans, now I can only invite 2 of you...")

no_longer_invited = guest_list.pop()

print(f"I'm very sorry but {no_longer_invited} you are no longer invited")

no_longer_invited = guest_list.pop()

print(f"I'm very sorry but {no_longer_invited} you are no longer invited")

no_longer_invited = guest_list.pop()

print(f"I'm very sorry but {no_longer_invited} you are no longer invited")

no_longer_invited = guest_list.pop()

print(f"I'm very sorry but {no_longer_invited} you are no longer invited")

print(f"I can't wait to see {guest_list[0]} and {guest_list[1]} in my party!")

del guest_list[1]
del guest_list[0]

print(guest_list)