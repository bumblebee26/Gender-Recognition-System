#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import shutil
import os

#Scrape  ----------------------------------------------------------------------------------------------

URL = "http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/"


def download_file(from_url, local_path):
    r = requests.get(from_url, stream=True)
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

def batch_download(matches):
    for match in matches:
        file_url = os.path.join(URL, match['href'])
        file_local = os.path.join('raw_zipped', match['href'])
        download_file(file_url, file_local)

def main():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    matches = soup.find_all('a', attrs={"href": re.compile("tgz")})

    if not os.path.exists('raw_zipped'): os.mkdir('raw_zipped')
    #raw_folder = os.path.join(__file__, 'raw')
    #raw_folder = os.path.join('.', 'raw')

    batch_download(matches)


if __name__ == '__main__':
	main()
