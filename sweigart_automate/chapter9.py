import os
from pathlib import Path


Path('spam', 'bacon', 'eggs')

# print(Path('spam', 'bacon', 'eggs'))
# print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

# for filename in myFiles:
#     print(Path(r'C:\Users\Al', filename))

# print(Path('spam') / 'bacon' / 'eggs')
# print(Path('spam') / Path('bacon/eggs'))
# print(Path('spam') / Path('bacon', 'eggs'))

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder

# print(homeFolder / subFolder)
# print(str(homeFolder / subFolder))


# print(Path.cwd())
# os.chdir('/mnt/d/PROGRAMOWANIE/GIT')
# print(Path.cwd())
# print(Path.home())

# os.makedirs('/mnt/d/PROGRAMOWANIE/nowy/folder')

# Path(r'/mnt/d/PROGRAMOWANIE/spam').mkdir()

# print(Path('my/relative/path'))

# print(Path.cwd() / Path('my/relative/path'))
#     print()

# print(os.path.abspath('.'))
# print(os.path.abspath('./Scripts'))

p = Path('C:/Users/Al/spam.txt')
p = Path('/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/spam.txt')
print(p.anchor)
print(p.parent)  # This is a Path object, not a string.
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)  # only on Windows, on Linux nothing
