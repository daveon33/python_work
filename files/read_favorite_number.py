from pathlib import Path
import json

def read_number():
    """"Reads the favorite number of the user """
    path = Path('files/text_files/favorite_number.json')
    contents = path.read_text()
    number = json.loads(contents)
    print(number)

read_number()