# https://realpython.com/python-json/
# 4/10

#! A Simple Serialization Example
import requests
import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# with open("data_file.json", "w") as write_file:
#     # json.dump(a, b) takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.
#     json.dump(data, write_file)

#     # json.dumps(a) - If you want to continue using this serialized JSON data in your program, you could write it to a native Python str object
#     print(json_string = json.dumps(data))
#     print(print(json_string))


#! Some Useful Keyword Arguments
# Both the dump() and dumps() methods use the same keyword arguments.
# The first option most people want to change is whitespace. You can use the indent keyword argument to specify the indentation size for nested structures.

# print(json.dumps(data))
# # {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}

# print(json.dumps(data, indent=4))
# # {
# #     "president": {
# #         "name": "Zaphod Beeblebrox",
# #         "species": "Betelgeusian"
# #     }
# # }

#! Deserializing JSON

# . That basically means that if you encode an object now and then decode it again later, you may not get exactly the same object back. I imagine it’s a bit like teleportation: break my molecules down over here and put them back together over there. Am I still the same person?

# blackjack_hand = (8, "Q")
# encoded_hand = json.dumps(blackjack_hand)
# print('encoded_hand: ', encoded_hand)

# decoded_hand = json.loads(encoded_hand)
# print('decoded_hand: ', decoded_hand)

# print('blackjack_hand == decoded_hand: ', blackjack_hand == decoded_hand)

# print('type(blackjack_hand): ', type(blackjack_hand))

# print('type(decoded_hand): ', type(decoded_hand))

# print('blackjack_hand == tuple(decoded_hand): ', blackjack_hand == tuple(decoded_hand))
# encoded_hand:  [8, "Q"]
# decoded_hand:  [8, 'Q']
# blackjack_hand == decoded_hand:  False
# type(blackjack_hand):  <class 'tuple'>
# type(decoded_hand):  <class 'list'>
# blackjack_hand == tuple(decoded_hand):  True

#! A Simple Deserialization Example

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)

#     print(type(data))
#     # <class 'dict'>
#     print(data)
#     # {'president': {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian'}}


#! A Real World Example

# You’ll need to make an API request to the JSONPlaceholder service

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# print('todos: ', todos)
# # todos:  [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False},

# print('todos == response.json(): ', todos == response.json())
# print('type(todos): ', type(todos))
# print('todos[:10]: ', todos[:10])
# # todos == response.json():  True
# # type(todos):  <class 'list'>
# # todos[:10]:  [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui',...


# There are multiple users, each with a unique userId, and each task has a Boolean completed property. Can you determine which users have completed the most tasks?

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

print('todos_by_user: ', todos_by_user)
print('todos_by_user.items(): ', todos_by_user.items())


# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print('top_users: ', top_users)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]
print('max_complete: ', max_complete)

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

# Create a string of user IDs with equal top tasks completed
max_users = " and ".join(users)
print('max_users: ', max_users)

# Add 's' to 'user' if there is more then one user on 1st place
s = "s" if len(users) > 1 else ""
# Print result
print(f"user{s} {max_users} completed {max_complete} TODOs")
