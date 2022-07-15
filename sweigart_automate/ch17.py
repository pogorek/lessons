# 17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS
import datetime
import time

#! The time Module
# The time.time() Function

# import time
# time.time()
# print('time.time(): ', time.time())
# # 1543813875.3518236
# x = (time.time() - 1543813875.3518236) / 60 / 60 / 24 / 365
# print(x)


# import time
# def calcProd():
#     # Calculate the product of the first 100,000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))


# import time
# print(time.ctime())
# # 'Mon Jun 15 14:00:38 2020'
# thisMoment = time.time()
# print(time.ctime(thisMoment))
# # 'Mon Jun 15 14:00:45 2020'

# The time.sleep() Function

# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

# Rounding Numbers

# import time
# now = time.time()
# print(now)
# # 1543814036.6147408
# print(round(now, 2))
# # 1543814036.61
# print(round(now, 4))
# # 1543814036.6147
# print(round(now))
# # 1543814037

# Project: Super Stopwatch

#! The datetime Module
# import datetime
# print(datetime.datetime.now())
# # 2022-07-06 00:56:28.409890
# dt = datetime.datetime(2019, 10, 21, 16, 29, 0, 666)
# print(dt)
# # 2019-10-21 16:29:00.000666
# print(dt.year, dt.month, dt.day)
# # (2019, 10, 21)
# print(dt.hour, dt.minute, dt.second)
# # (16, 29, 0)

# import datetime, time
# print(datetime.datetime.fromtimestamp(1000000))
# # 1970-01-12 14:46:40
# print(datetime.datetime.fromtimestamp(time.time()))
# # 2022-07-06 00:58:30.280009

# import datetime
# halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# print(halloween2019 == oct31_2019) # True
# print(halloween2019 > newyears2020) # False
# print(newyears2020 > halloween2019) # True
# print(newyears2020 != oct31_2019) # True

# # The timedelta Data Type

# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# # (11, 36548, 0)
# print(delta.total_seconds())
# # 986948.0
# print(str(delta))
# # '11 days, 10:09:08'

# # calculate the date 1,000 days from now
# dt = datetime.datetime.now()
# print(dt)
# # 2022-07-06 01:11:02.181184
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)
# # 2025-04-01 01:11:02.181184

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)
# # 2019-10-21 16:29:00
# print(oct21st - aboutThirtyYears)
# # 1989-10-28 16:29:00
# print(oct21st - (2 * aboutThirtyYears))
# # 1959-11-05 16:29:00

# ## Pausing Until a Specific Date

# import datetime
# import time
# halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

# Converting datetime Objects into Strings

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# # '2019/10/21 16:29:00'
# print(oct21st.strftime('%I:%M %p'))
# # '04:29 PM'
# print(oct21st.strftime("%B of '%y"))
# # "October of '19"

# Converting Strings into datetime Objects

# print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
# # 2019-10-21 00:00:00
# print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# # 2019-10-21 16:29:00
# print(datetime.datetime.strptime("October of '19", "%B of '%y"))
# # 2019-10-01 00:00:00
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))
# # 2063-11-01 00:00:00

#! Multithreading

import threading
# import time
# print('Start of program.')

# def takeANap():
#     time.sleep(5)
#     print('Wake up!')

# threadObj = threading.Thread(target=takeANap)
# threadObj.start()

# print('End of program.')

# Passing Arguments to the Thread’s Target Function

# threadObj = threading.Thread(
#     target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# threadObj.start()
# # Cats & Dogs & Frogs

#! Project: Multithreaded XKCD Downloader

#! Launching Other Programs from Python

import subprocess
# # subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# print(subprocess.Popen('/mnt/c/Windows/System32/calc.exe'))

# paintProc = subprocess.Popen('/mnt/c/Windows/System32/mspaint.exe')
# print(paintProc.poll() == None)
# # True
# print(paintProc.wait())  # Doesn't return until MS Paint closes.
# # 0
# print(paintProc.poll())
# # 0

# Passing Command Line Arguments to the Popen() Function

# subprocess.Popen(['/mnt/c/Windows/notepad.exe',
#                  'D:\\PROGRAMOWANIE\\GIT\\school\\sweigart_automate\\hello.txt'])
# subprocess.Popen(['/mnt/c/Windows/notepad.exe',
#                  r'D:\PROGRAMOWANIE\GIT\school\sweigart_automate\hello.txt'])
# subprocess.Popen(['/mnt/c/Program Files/Notepad++/notepad++.exe',
#                  '/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/hello.txt'])

# Task Scheduler, launchd, and cron

# Opening Websites with Python

# Running Other Python Scripts
# subprocess.Popen(['/mnt/c/Users/Piotr/AppData/Local/Programs/Python/Python310/python.exe', 'hello.py']) # OK

# subprocess.Popen(['python3', 'hello.py']) # OK

# subprocess.run(["python3", "hello.py"]) # OK

# subprocess.Popen(
#     [r'C:\Users\Piotr\AppData\Local\Programs\Python\Python310\python.exe', 'hello.py']) # Don't work
# subprocess.Popen(
#     ['C:\Users\Piotr\AppData\Local\Programs\Python\Python310\python.exe', 'hello.py']) # Don't work
# subprocess.Popen(
#     ['C:\\Users\\Piotr\\AppData\\Local\\Programs\\Python\\Python310\\python.exe', 'hello.py']) # Don't work

# Opening Files with Default Applications

fileObj = open('hello.txt', 'w')
fileObj.write('Hello, world YO!')
# 12
fileObj.close()
filepath = '/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate/hello.txt'
# no - hello.txt: 1: cmd: not found
# subprocess.Popen(['cmd /c start', 'hello.txt'], shell=True)
# subprocess.Popen(['start', 'hello.txt'], shell=True) # no - hello.txt: 1: start: not found
# subprocess.Popen(['xdg-open', 'hello.txt'], shell=True) # no - hello.txt: 1: xdg-open: not found
# subprocess.Popen(['see', 'hello.txt']) # no - hello.txt: 1: see: not found

# subprocess.call(('start', 'hello.txt'), shell=True) # no - hello.txt: 1: start: not found

# subprocess.run(['open', filepath], check=True) # no - FileNotFoundError: [Errno 2] No such file or directory: 'open'
# subprocess.run(['xdg-open', filepath], check=True) # no - FileNotFoundError: [Errno 2] No such file or directory: 'xdg-open'
# subprocess.run(['xdg-open', 'hello.txt'], check=True) # no - FileNotFoundError: [Errno 2] No such file or directory: 'xdg-open'
# subprocess.run(['see', filepath], check=True) # strange

# subprocess.check_call(['open', filepath]) # no - FileNotFoundError: [Errno 2] No such file or directory: 'open'
# subprocess.check_call(['xdg-open', filepath]) # no - FileNotFoundError: [Errno 2] No such file or directory: 'xdg-open'
# subprocess.check_call(['start', filepath]) # no - FileNotFoundError: [Errno 2] No such file or directory: 'start'

# subprocess.check_call(['see', filepath]) # strange

#! Project: Simple Countdown Program
