from pathlib import Path
import json

def favorite_number():
    """"Asks the user for their favorite number and stores it in a JSON file"""
    path = Path('files/text_files/favorite_number.json')
    number = input('What\'s your favorite number? ')
    contents = json.dumps(number)
    path.write_text(contents)

favorite_number()
