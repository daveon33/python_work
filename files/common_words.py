from pathlib import Path

path = Path('files/text_files/pride_and_prejudice.txt')
contents = path.read_text(encoding="utf-8").splitlines()
counting_words = ""

for line in contents:
    counting_words += line
print(counting_words.count('the'))
print(counting_words.count('the '))