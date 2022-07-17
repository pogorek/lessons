#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading

os.makedirs('xkcd3', exist_ok=True)    # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading threaded 40 page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading threaded 40 image no %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join(
                'xkcd3', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 2640, 40):    # loops times, creates 14 threads
    start = i
    end = i + 39
    if start == 0:
        start = 1  # There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# TODO: Wait for all threads to end.
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Threaded done.')
