# 12 WEB SCRAPING

# import webbrowser
# webbrowser.open('https://inventwithpython.com/')

## Downloading Files from the Web with the requests Module

# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# # <class 'requests.models.Response'>
# print(res.status_code == requests.codes.ok)
# # True
# print(len(res.text))
# # 178981
# print(res.text[:250])

## Checking for Errors

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()

# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

## Saving Downloaded Files to the Hard Drive

# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()

### HTML
# ... 

## Parsing HTML with the bs4 Module

## Creating a BeautifulSoup Object from HTML
# import requests, bs4
# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# type(noStarchSoup)
# # <class 'bs4.BeautifulSoup'>

# # You can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup()
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
# type(exampleSoup)
# # <class 'bs4.BeautifulSoup'>

## Finding an Element with the select() Method

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems)) # elems is a list of Tag objects.
# # <class 'list'>
# print(len(elems))
# # 1
# print(type(elems[0]))
# # <class 'bs4.element.Tag'>
# print(str(elems[0])) # The Tag object as a string.
# # '<span id="author">Al Sweigart</span>'
# print(elems[0].getText())
# # 'Al Sweigart'
# print(elems[0].attrs)
# # {'id': 'author'}

pElems = exampleSoup.select('p')
str(pElems[0])
print('str(pElems[0]): ', str(pElems[0]))
# '<p>Download my <strong>Python</strong> book from <a href="https://inventwithpython.com">my website</a>.</p>'
pElems[0].getText()
print('pElems[0].getText(): ', pElems[0].getText())
# 'Download my Python book from my website.'
str(pElems[1])
print('str(pElems[1]): ', str(pElems[1]))
# '<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
print('pElems[1].getText(): ', pElems[1].getText())
# 'Learn Python the easy way!'
str(pElems[2])
print('str(pElems[2]): ', str(pElems[2]))
# '<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()
print('pElems[2].getText(): ', pElems[2].getText())
# 'By Al Sweigart'
print('str(pElems): ', str(pElems))


## Getting Data from an Element’s Attributes

# import bs4
# soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
# spanElem = soup.select('span')[0]
# str(spanElem)
# # '<span id="author">Al Sweigart</span>'
# spanElem.get('id')
# # 'author'
# spanElem.get('some_nonexistent_addr') == None
# # True
# spanElem.attrs
# # {'id': 'author'}

#! Project: Opening All Search Results
# searchpypi.py

#! Project: Downloading All XKCD Comics
# downloadXkcd.py