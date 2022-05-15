# 10 ORGANIZING FILES

#! The shutil Module
## Copying Files and Folders

import shutil, os
from pathlib import Path
p = Path.cwd()
# print(shutil.copy(p / 'spam.txt', p / 'some_folder'))
# print(shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt'))

# import shutil, os
from pathlib import Path
p = Path.cwd()
# print(shutil.copytree(p / 'some_folder', p / 'some_folder_backup'))

# Moving and Renaming Files and Folders




