# https://www.programiz.com/python-programming/json
# https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/

#? Serialization: converting an object into a JSON string.
#? Deserialization: converting a JSON string into an object.

#? json.load() vs. json.loads()
## json.load()
# Purpose: Create Python object(dictionary) from a JSON file
# Argument: JSON file
# Return value: Python object(dictionary)


## json.loads()
# Purpose: Create Python object(dictionary) from a string
# Argument: String
# Return value: Python object(dictionary)

#? json.dump() vs. json.dumps()
## json.dump()
# Purpose: Write object(for example, a dictionary) in JSON format to a file
# Argument: Object(dictionary) + File
# Return value: None

## json.dumps()
# Purpose: Get a JSON string from an object(for example, a dictionary)
# Argument: Object(dictionary) 
# Return value: String


#! Example 1: Python JSON to dict
## You can parse a JSON string using json.loads() method. The method returns a dictionary.
## Here, person is a JSON string, and person_dict is a dictionary.

# json.loads(person) creates a new dictionary with the key-value pairs of the JSON string and it returns new dictionary.
# Then, the dictionary returned is assigned to the variable person_dict.

import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

#! Example 2: Python read JSON file
## You can use json.load() method to read a file containing JSON object.
## Suppose, you have a file named person.json which contains a JSON object.

## {"name": "Bob",
## "languages": ["English", "French"]
## }

## Here, we have used the open() function to read the json file.
## Then, the file is parsed using json.load() method which gives us a dictionary named data.

# json.load(file) creates and returns a new Python dictionary with the key-value pairs in the JSON file.
# Then, this dictionary is assigned to the data variable.

with open('person.json', 'r') as file:
    data = json.load(file)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)


#! Example 3: Convert dict to JSON
## You can convert a dictionary to JSON string using json.dumps() method.

# json.dumps(person_dict) creates and returns a string with all the key-value pairs of the dictionary in JSON format.
# Then, this string is assigned to the person_json variable.

import json

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)



#! Example 4: Writing JSON to a file
## To write JSON to a file in Python, we can use json.dump() method.
## In this program, we have opened a file named person.json in writing mode using 'w'. If the file doesn't already exist, it will be created. Then, json.dump() transforms person_dict to a JSON string which will be saved in the person.json file.

# This is a function that takes two arguments:
# The object that will be stored in JSON format (for example, a dictionary person_dict).
# The file where it will be stored (for example, a new file object).

import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

# We can write it to txt(or any we want) or json file like 'json_file.json'
with open('person.json', 'w') as json_file:
    json.dump(person_dict, json_file)

# person.json:
# {"name": "Bob", "languages": ["English", "French"], "married": true, "age": 32}


#! Example 5: Python pretty print JSON
## To analyze and debug JSON data, we may need to print it in a more readable format. This can be done by passing additional parameters indent and sort_keys to json.dumps() and json.dump() method.

## In this program, we have used 4 spaces for indentation. And, the keys are sorted in ascending order.

## By the way, the default value of indent is None. And, the default value of sort_keys is False.

import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Without additional arguments
print(json.dumps(person_dict))
# {"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))
# {
#     "languages": "English",
#     "name": "Bob",
#     "numbers": [
#         2,
#         1.6,
#         null
#     ]
# }
