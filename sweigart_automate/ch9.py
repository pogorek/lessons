import os
from pathlib import Path


# Path('spam', 'bacon', 'eggs')

# # print(Path('spam', 'bacon', 'eggs'))
# # print(str(Path('spam', 'bacon', 'eggs')))

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

# # for filename in myFiles:
# #     print(Path(r'C:\Users\Al', filename))

# # print(Path('spam') / 'bacon' / 'eggs')
# # print(Path('spam') / Path('bacon/eggs'))
# # print(Path('spam') / Path('bacon', 'eggs'))

# homeFolder = Path('C:/Users/Al')
# subFolder = Path('spam')
# homeFolder / subFolder

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

# p = Path('C:/Users/Al/spam.txt')
# p = Path('/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/spam.txt')
# print(p.anchor)
# print(p.parent)  # This is a Path object, not a string.
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.drive)  # only on Windows, on Linux nothing

# Finding File Sizes and Folder Contents

# cwd = Path.cwd()
# file_ = "chapter8.py"
# # print('cwd: ', cwd / file_)

# file_size = os.path.getsize(cwd / file_)
# # print('file_size: ', file_size)

# cwd_listdir = os.listdir(cwd)
# print('cwd_listdir: ', cwd_listdir)

# totalSize = 0
# for filename in os.listdir(cwd):
#     totalSize = totalSize + os.path.getsize(os.path.join(cwd, filename))
# # print(totalSize)

# ## Modifying a List of Files Using Glob Patterns

# p = Path.cwd()
# # print(p.glob('*'))

# p_glob_list = list(p.glob('*'))  # Make a list from the generator.
# print('p_glob_list: ', p_glob_list)

# print("2: ", list(p.glob('*.txt')))  # Lists all text files.

# print("3: ",  list(p.glob('chapter?.py')))


# for file in p.glob('*.txt'):
#     print(file)  # Prints the Path object as a string.
#     # Do something with the text file.


# Checking Path Validity

# winDir = Path('/mnt/c/Windows')
# notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
# calcFile = Path('/mnt/c/Windows/System32/calc.exe')
# print(winDir.exists()) # True
# print(winDir.is_dir()) # True
# print(notExistsDir.exists()) # False
# print(calcFile.is_file()) # True
# print(calcFile.is_dir()) # False

# The File Reading/Writing Process
# Opening Files with the open() Function

helloFile = open(Path.cwd() / 'hello.txt')
# print('helloFile: ', helloFile)
# # helloFile:  <_io.TextIOWrapper name='/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/hello.txt' mode='r' encoding='UTF-8'>
# helloFile2 = open('/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/hello.txt')
# # print('helloFile2: ', helloFile2)

# helloFile3 = open(Path.cwd() / 'hello.txt', 'r')
# # print('helloFile3: ', helloFile3)

# ## Reading the Contents of Files

# helloContent = helloFile.read()
# print('helloContent: ', helloContent)

sonnetFile = open(Path.cwd() / 'sonnet29.txt')
print(helloFile.readlines())
# # for line in sonnetFile.readlines():
# #     print(line, end="")
# # print()

# ## Writing to Files

# baconFile = open('bacon.txt', 'w')
# baconFile.write('Hello, world!\n')
# baconFile.close()

# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()

# baconFile = open('bacon.txt')
# content = baconFile.read()
# baconFile.close()
# # print(content)

# ## Saving Variables with the shelve Module

# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# # <class 'shelve.DbfilenameShelf'>
# print(shelfFile['cats'])
# # ['Zophie', 'Pooka', 'Simon']
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# # print(list(shelfFile.keys()))
# # ['cats']
# # print(list(shelfFile.values()))
# # [['Zophie', 'Pooka', 'Simon']]
# shelfFile.close()

# ## Saving Variables with the pprint.pformat() Function

# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# # print('cats: ', type(cats)) # list
# pprint.pformat(cats) # "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
# # print('cats: ', type(pprint.pformat(cats))) # str
# # print('cats: ', type(cats)) # list
# fileObj = open('myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()

# import myCats
# # print(myCats.cats) # [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# # print(myCats.cats[0]) # {'name': 'Zophie', 'desc': 'chubby'}
# # print(myCats.cats[0]['name']) # 'Zophie'
