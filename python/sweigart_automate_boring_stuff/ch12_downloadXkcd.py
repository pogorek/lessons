#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'https://xkcd.com'               # starting url

# The call os.makedirs() ensures that this folder exists, and the exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists.
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd

# End the loop when url ends with '#'.
while not url.endswith('#'):
    # ? Download the page.

    # Print url so that the user knows which URL the program is about to download
    print('Downloading R page %s...' % url)

    # Use the requests module’s request.get() function to download it
    res = requests.get(url)
    # Check if download was successful
    res.raise_for_status()

    # Create a BeautifulSoup object from the text of the downloaded page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # ? Find the URL of the comic image.

    # From inspecting the XKCD home page with your developer tools, you know that selector '#comic img' will get you the correct <img> element from the BeautifulSoup object
    comicElem = soup.select('#comic img')

    # If your selector doesn’t find any elements, then soup.select('#comic img') will return a blank list. Print an error message and move on without downloading the image.
    if comicElem == []:
        print('Could not find comic image.')
    # Otherwise, the selector will return a list containing one <img> element
    else:
        # Get the src attribute from this <img> element
        # 'https://imgs.xkcd.com/comics/heartbleed_explanation.png'
        comicUrl = 'https:' + comicElem[0].get('src')

        # print(comicElem[0].get('src')) #  6 //imgs.xkcd.com/comics/or_whatever.png

        # Download the image.
        print('Downloading R image %s...' % (comicUrl))

        # Pass src to requests.get() to download the comic’s image file.
        res = requests.get(comicUrl)
        res.raise_for_status()

        # ? Save the image to ./xkcd.
        # os.path.basename(comicUrl) - 'or_whatever.png'
        # Join this name with the name of your xkcd folder using os.path.join() so that your program uses backslashes (\) on Windows and forward slashes (/) on macOS and Linux.
        imageFile = open(os.path.join(
            'xkcd', os.path.basename(comicUrl)), 'wb')
        # print("os.path.join('xkcd': ", os.path.join('xkcd', os.path.basename(comicUrl)))
        # print('os.path.basename(comicUrl): ', os.path.basename(comicUrl))

        # Loop over the return value of the iter_content() method
        for chunk in res.iter_content(100000):
            # Write out chunks of the image data (at most 100,000 bytes each) to the file
            imageFile.write(chunk)
        # Close the file
        imageFile.close()

    # ? Get the Prev button's url.
    # Selector 'a[rel="prev"]' identifies the <a> element with the rel attribute set to prev
    prevLink = soup.select('a[rel="prev"]')[0]

    # Get the previous comic’s URL
    url = 'https://xkcd.com' + prevLink.get('href')

print('Regular done.')
