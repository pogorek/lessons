# 17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS17 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS

#! The time Module
## The time.time() Function

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

## The time.sleep() Function

# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

## Rounding Numbers

import time
now = time.time()
print(now)
# 1543814036.6147408
print(round(now, 2))
# 1543814036.61
print(round(now, 4))
# 1543814036.6147
print(round(now))
# 1543814037