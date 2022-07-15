# 16 WORKING WITH CSV FILES AND JSON DATA


#! The csv Module
## reader Objects

# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# # [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],

# exampleData[0][0]
# # '4/5/2015 13:34'
# exampleData[0][1]
# # 'Apples'

## Reading Data from reader Objects in a for Loop

# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# Row #1 ['4/5/2015 13:34', 'Apples', '73']
# Row #2 ['4/5/2015 3:41', 'Cherries', '85'] ...

## writer Objects
# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
# # 21
# print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
# # 32
# print(outputWriter.writerow([1, 2, 3.141592, 4]))
# # 16
# outputFile.close()

## The delimiter and lineterminator Keyword Arguments

# import csv
# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# # 24
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# # 17
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# # 32
# csvFile.close()

## DictReader and DictWriter CSV Objects

# import csv
# exampleFile = open('automate_online-materials/exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)
# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])


# import csv
# exampleFile = open('example.csv')
# exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',
# 'amount'])
# for row in exampleDictReader:
#     print(row['time'], row['name'], row['amount'])


# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
# outputDictWriter.writeheader()
# outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
# # 20
# outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
# # 15
# outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':
# 'dog'})
# # 20
# outputFile.close()


#! JSON and APIs
## Reading JSON with the loads() Function

# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# import json
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)
# # {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

## Writing JSON with the dumps() Function

# pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
# import json
# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)
# # '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'

#! Project: Fetching Current Weather Data


