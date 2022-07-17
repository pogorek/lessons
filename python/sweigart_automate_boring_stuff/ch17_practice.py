
import subprocess
import time


# url = 'https://xkcd.com'               # starting url

# img_count = 0
# while not url.endswith('#'):
#     img_count += 1

#     print('Downloading page %s...' % url)

#     # Use the requests module’s request.get() function to download it
#     res = requests.get(url)
#     # Check if download was successful
#     res.raise_for_status()

#     # Create a BeautifulSoup object from the text of the downloaded page
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')

#     prevLink = soup.select('a[rel="prev"]')[0]

#     # Get the previous comic’s URL
#     url = 'https://xkcd.com' + prevLink.get('href')

# print(img_count)


# Threaded download 10
threadedStartTime = time.time()
download_t = subprocess.Popen(['python3', 'ch17_threadedDownloadXkcd2.py'])
download_t.wait()
threadedEndTime = time.time()

# Regular download
startTime = time.time()
download_r = subprocess.Popen(['python3', 'ch12_downloadXkcd.py'])
download_r.wait()
endTime = time.time()

# Threaded download 40
threadedStartTime3 = time.time()
download_t3 = subprocess.Popen(['python3', 'ch17_threadedDownloadXkcd3.py'])
download_t3.wait()
threadedEndTime3 = time.time()


print()
print('Regular download took %s minutes to complete.' %
      (round(endTime - startTime) / 60))

print('Threaded download 10 took %s minutes to complete.' %
      (round(threadedEndTime - threadedStartTime) / 60))

print('Threaded download 40 took %s minutes to complete.' %
      (round(threadedEndTime3 - threadedStartTime3) / 60))
