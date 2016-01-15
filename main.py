import requests
from bs4 import BeautifulSoup

PLAYLIST_URL = 'https://www.youtube.com/watch?v=HjuHHI60s44&index=1&list=PL6gx4Cwl9DGCkg2uj3PxUWhMDuTw3VKjM'
video_codes = []
video_titles = []


def crawl(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for playlist in soup.findAll('div', {'class': 'playlist-videos-container'}):
        for link in playlist.findAll('a'):
            results = link.get('href')
            video_codes.append(results[9:20])
        for title in playlist.findAll('h4'):
            video_titles.append(title.string.strip())


def test():
    for x, y in enumerate(video_codes):
        print(video_codes[x] + '\t\t' + video_titles[x])


crawl(PLAYLIST_URL)
test()
