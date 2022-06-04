# 12 WEB SCRAPING

# import webbrowser
# webbrowser.open('https://inventwithpython.com/')

# Downloading Files from the Web with the requests Module

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
# <class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)
# True
print(len(res.text))
# 178981
print(res.text[:250])
