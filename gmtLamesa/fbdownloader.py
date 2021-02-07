import re
import requests
import urllib.request

# video link
link = input("Video Url : ")

# read html data
html = requests.get(link)

# parse url
try:
    url = re.search('hd_src:"(.+?)"',html.text)[1]
    print("HD Video")
except:
    url = re.search('sd_src:"(.+?)"',html.text)[1]
    print("SD Video")

# download file
print("Downloading . . .")
urllib.request.urlretrieve(url, "Facebook Video.mp4")
print("Downloaded Sucessfully!")
