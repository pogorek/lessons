# https://realpython.com/api-integration-in-python/
# Python and REST APIs: Interacting With Web Services
# 18.07.22

"""
In this tutorial, you’ll learn:
What REST architecture is
How REST APIs provide access to web data
How to consume data from REST APIs using the requests library
What steps to take to build a REST API
What some popular Python tools are for building REST APIs
"""
## Data available on the Web(YouTube and GitHub) is accessible to third-party applications through an application programming interface (API). 
## One of the most popular ways to build APIs is the REST architecture style. 
## Python provides some great tools not only to get data from REST APIs but also to build your own Python REST APIs.
## By using Python and REST APIs, you can retrieve, parse, update, and manipulate the data provided by any web service you’re interested in.
## REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. 

#! REST APIs and Web Services
## A REST web service is any web service that expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.

# For example, here’s one of the URLs for GitHub’s REST API:
# https://api.github.com/users/<username>

#! HTTP Methods

## REST APIs listen for HTTP methods to know which operations to perform on the web service’s resources. A resource is any data available in the web service that can be accessed and manipulated with HTTP requests to the REST API. The HTTP method tells the API which action to perform on the resource.

# HTTP method	    Description
# GET	            Retrieve an existing resource.
# POST	            Create a new resource.
# PUT	            Update an existing resource.
# PATCH	            Partially update an existing resource.
# DELETE	        Delete a resource.

#! Status Codes
## Once a REST API receives and processes an HTTP request, it will return an HTTP response. Included in this response is an HTTP status code. This code provides information about the results of the request. An application sending requests to the API can check the status code and perform actions based on the result. These actions could include handling errors or displaying a success message to a user.

# Code	    Meaning	        Description
# 200	    OK	            The requested action was successful.
# 201	    Created	        A new resource was created.
# 202	    Accepted	    The request was received, but no modification has been made yet.
# 204	    No Content	    The request was successful, but the response has no content.
# 400	    Bad Request	    The request was malformed.
# 401	    Unauthorized	The client is not authorized to perform the requested action.
# 404	    Not Found	                The requested resource was not found.
# 415	    Unsupported Media Type	    The request data format is not supported by the server.
# 422	    Unprocessable Entity	    The request data was properly formatted but contained invalid or missing data.
# 500	    Internal Server Error	    The server threw an error when processing the request.

# Code range	Category
# 2xx	        Successful operation
# 3xx	        Redirection
# 4xx	        Client error
# 5xx	        Server error

#! API Endpoints
## A REST API exposes a set of public URLs that client applications use to access the resources of a web service. These URLs, in the context of an API, are called endpoints.

## To help clarify this, take a look at the table below. In this table, you’ll see API endpoints for a hypothetical CRM system. These endpoints are for a customer resource that represents potential customers in the system:

# HTTP method	API endpoint	        Description
# GET	    /customers	                Get a list of customers.
# GET	    /customers/<customer_id>	Get a single customer.
# POST	/customers	                Create a new customer.
# PUT	    /customers/<customer_id>	Update a customer.
# PATCH	/customers/<customer_id>	Partially update a customer.
# DELETE	/customers/<customer_id>	Delete a customer.
# Each of the endpoints above performs a different action based on the HTTP method.

# Note: The base URL for the endpoints has been omitted for brevity. In reality, you’ll need the full URL path to access an API endpoint: https://api.example.com/customers

#! REST and Python: Consuming APIs
## To write code that interacts with REST APIs, most Python developers turn to requests to send HTTP requests. 
# pip3 install requests

#! GET
## This method allows you to retrieve resources from a given API. 
## GET is a read-only operation, so you shouldn’t use it to modify an existing resource.

# This code calls requests.get() to send a GET request to /todos/1, which responds with the todo item with the ID 1. Then you can call .json() on the response object to view the data that came back from the API.
# The response data is formatted as JSON, a key-value store similar to a Python dictionary.
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# print('response.status_code: ', response.status_code)
# # response.status_code:  200

# print('response.headers["Content-Type"]: ', response.headers["Content-Type"])
# # response.headers["Content-Type"]:  application/json; charset=utf-8

# Here, you access response.status_code to see the HTTP status code. You can also view the response’s HTTP headers with response.headers. This dictionary contains metadata about the response, such as the Content-Type of the response.


#! POST
## Use requests to POST data to a REST API to create a new resource. 
## You’ll use JSONPlaceholder again, but this time you’ll include JSON data in the request. 

# Create a dictionary containing the data for your todo.
# Pass this dictionary to the json keyword argument of requests.post(). 
# Call requests.post() to create a new todo in the system.
# When you do this, requests.post() automatically sets the request’s HTTP header Content-Type to application/json. 
# It also serializes todo into a JSON string, which it appends to the body of the request.

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
# print('response.status_code: ', response.status_code)
# # response.status_code:  201

## If you don’t use the json keyword argument to supply the JSON data, then you need to set Content-Type accordingly and serialize the JSON manually.

# In this code, you add a headers dictionary that contains a single header Content-Type set to application/json. This tells the REST API that you’re sending JSON data with the request.

# You then call requests.post(), but instead of passing todo to the json argument, you first call json.dumps(todo) to serialize it. After it’s serialized, you pass it to the data keyword argument. The data argument tells requests what data to include in the request. You also pass the headers dictionary to requests.post() to set the HTTP headers manually.

# When you call requests.post() like this, it has the same effect as the previous code but gives you more control over the request.

# import requests
# import json
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# response.json()

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
# print('response.status_code: ', response.status_code)
# # response.status_code:  201

# Once the API responds, you call response.json() to view the JSON. The JSON includes a generated id for the new todo. The 201 status code tells you that a new resource was created.


#! PUT
## Sends a PUT request to update an existing todo with new data. 
## Any data sent with a PUT request will completely replace the existing values of the todo.

# You’ll use the same JSONPlaceholder endpoint you used with GET and POST, but this time you’ll append 10 to the end of the URL. This tells the REST API which todo you’d like to update:

# Here, you first call requests.get() to view the contents of the existing todo. 
# Next, you call requests.put() with new JSON data to replace the existing todo’s values. You can see the new values when you call response.json(). 
# Successful PUT requests will always return 200 instead of 201 because you aren’t creating a new resource but just updating an existing one.

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'id': 10, 'title': 'illo est ratione doloremque quia maiores aut', 'completed': True}

# todo = {"userId": 1, "title": "Wash car", "completed": True}
# response = requests.put(api_url, json=todo)

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}

# print('response.status_code: ', response.status_code)
# # response.status_code:  200


#! PATCH
## Modify the value of a specific field on an existing todo. 
## PATCH differs from PUT in that it doesn’t completely replace the existing resource. It only modifies the values set in the JSON sent with the request.

# You’ll use the same todo from the last example to try out requests.patch(). Here are the current values:
# {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}

# Now you can update the title with a new value:

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# todo = {"title": "Mow lawn"}
# response = requests.patch(api_url, json=todo)

# print('response.json(): ', response.json())
# # response.json():  {'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

# print('response.status_code: ', response.status_code)
# # response.status_code:  200


#! DELETE
## DELETE completely removes a resource. 

# You call requests.delete() with an API URL that contains the ID for the todo you would like to remove. 
# This sends a DELETE request to the REST API, which then removes the matching resource. 
# After deleting the resource, the API sends back an empty JSON object indicating that the resource has been deleted.

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)

print('response.json(): ', response.json())
# response.json():  {}

print('response.status_code: ', response.status_code)
# response.status_code:  200

#! REST and Python: Building APIs

## Identify Resources
#The first step you’ll take as you build a REST API is to identify the resources the API will manage. It’s common to describe these resources as plural nouns, like customers, events, or transactions. 

## Define Your Endpoints
# Once you’ve identified the resources in your web service, you’ll want to use these to define the API endpoints. 

## Pick Your Data Interchange Format
# Two popular options for formatting web service data are XML and JSON. 

## Design Success Responses
# Once you’ve picked a data format, the next step is to decide how you’ll respond to HTTP requests. All responses from your REST API should have a similar format and include the proper HTTP status code.

# Response has a 201 Created status code to tell the user that a new resource was created. Make sure to use 201 Created instead of 200 OK for all successful POST requests.

# It’s important to always send back a copy of a resource when a user creates it with POST or modifies it with PUT or PATCH. This way, the user can see the changes that they’ve made.

## Design Error Responses

# There’s always a chance that requests to your REST API could fail. It’s a good idea to define what an error response will look like. These responses should include a description of what error occurred along with the appropriate status code. 

#! REST and Python: Tools of the Trade
# In this section, you’ll look at three popular frameworks for building REST APIs in Python.

#! Django REST Framework

# First, install Django and djangorestframework with pip:
pip3 install Django djangorestframework

