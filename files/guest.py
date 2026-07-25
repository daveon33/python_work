from pathlib import Path

path = Path('files\guest.txt')
new_guest = input('What is your name? ')
path.write_text(new_guest)