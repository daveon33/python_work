from pathlib import Path

files = ['files/text_files/cats.txt', 'files/text_files/dogs.txt']

for file in files:
    try:
        path = Path(file)
        print(path.read_text())
    except FileNotFoundError:
        pass


