from pathlib import Path

path = Path('files\guest.txt')
our_guests = ""

while(True):
    new_guest = input('What is your name? ')
    our_guests += new_guest + '\n'    
    guest_remaining = input('Are there any more guests? (Y/N): ')

    if guest_remaining == "Y" or guest_remaining == "y":
        continue
    else:
        break

path.write_text(our_guests)