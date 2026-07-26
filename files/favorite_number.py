from pathlib import Path
import json

def favorite_number():
    """"Asks the user for their favorite number and stores it in a JSON file"""
    path = Path('files/text_files/favorite_number.json')
    if path.exists():
        number = read_number(path)
        print(f'Your favorite number is: {number}')
        
    else:
        number = input('What\'s your favorite number: ')
        contents = json.dumps(number)
        path.write_text(contents)
        print('We saved your favorite number!')

def read_number(path):
    """"Reads the favorite number of the user """
    contents = path.read_text()
    number = json.loads(contents)
    return number

    
favorite_number()
