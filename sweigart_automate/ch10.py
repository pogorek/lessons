# 10 ORGANIZING FILES

#! The shutil Module
# Copying Files and Folders

import zipfile
import send2trash
import shutil
import os
from pathlib import Path
p = Path.cwd()
# print(shutil.copy(p / 'spam.txt', p / 'some_folder'))
# print(shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt'))

# import shutil, os
p = Path.cwd()
# print(shutil.copytree(p / 'some_folder', p / 'some_folder_backup'))

# Moving and Renaming Files and Folders
# import shutil

# ret = shutil.move('/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/bacon.txt',
#                   '/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/eggs')
# print('ret: ', ret)

# not working - must be a string path
# p1 = Path.cwd() / 'spam.txt'
# p2 = Path.cwd() / 'eggs'
# ret = shutil.move(p1, p2)
# print('ret: ', ret)

# ret = shutil.move('/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/bacon.txt',
#                   '/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/eggs/new_bacon.txt')
# print('ret: ', ret)

# Permanently Deleting Files and Folders
# # import os
# p = Path.cwd() / 'eggs'
# for filename in p.glob('*.txt'):
#     os.unlink(filename)
#     # print(filename)

# Safe Deletes with the send2trash Module
# pip3 install send2trash

# baconFile = open('bacon2.txt', 'a')   # creates the file
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash.send2trash('bacon2.txt')

# trying to find trash on linux on win - fail
# p = Path(Path.home() / 'local/share/trash')
# cwd_listdir = os.listdir(p)
# print('cwd_listdir: ', cwd_listdir)

# Walking a Directory Tree
# import os

# p = Path.cwd()
# for folderName, subfolders, filenames in os.walk(p):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': ' + filename)

#     print('')

#! Compressing Files with the zipfile Module
# Reading ZIP Files

# import zipfile

# p = Path.cwd()
# exampleZip = zipfile.ZipFile(p / 'spam.zip')
# print(exampleZip.namelist())
# #   ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
# spamInfo = exampleZip.getinfo('some_folder/spam.txt')
# print(spamInfo.file_size)
# #   13908
# print(spamInfo.compress_size)
# #   3828
# print(
#     f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
# #'Compressed file is 3.63x smaller!'
# exampleZip.close()

# Extracting from ZIP Files

# import zipfile, os
# p = Path.cwd()
# exampleZip = zipfile.ZipFile(p / 'spam.zip')
# exampleZip.extractall()
# exampleZip.close()

# p = Path.cwd()
# exampleZip = zipfile.ZipFile(p / 'spam.zip')
# exampleZip.extractall(p / 'to_extract')
# exampleZip.close()

# p = Path.cwd()
# exampleZip = zipfile.ZipFile(p / 'spam.zip')
# # exampleZip.extract('some_folder/spam.txt')
# # 'C:\\spam.txt'
# exampleZip.extract('some_folder/spam.txt', p / 'to_extract2')
# # 'C:\\some\\new\\folders\\spam.txt'
# exampleZip.close()

# Creating and Adding to ZIP Files
# import zipfile
# newZip = zipfile.ZipFile('new.zip', 'a')
# newZip.write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()
