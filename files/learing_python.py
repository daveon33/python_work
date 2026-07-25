from pathlib import Path

path = Path('files\learning_python.txt')
contents = path.read_text()
print(contents)

for line in contents.splitlines():
    print(line.replace('python', 'c'))
    


