# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:27:22 2019

@author: asuryana
"""
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib.request
import sys

import youtube_dl

query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
count=0
print("***************")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    count+=1
    print('https://www.youtube.com' + vid['href'])
    url = 'https://www.youtube.com' + vid['href']

    ydl_opts = {'preferredcodec': 'mp3'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    if(count==1):
        sys.exit(0);