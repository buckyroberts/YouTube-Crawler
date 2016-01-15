import requests
from bs4 import BeautifulSoup

CATEGORY = 373
PLAYLIST_URL = 'https://www.youtube.com/watch?v=qIULMnbH2-o&index=1&list=PL6gx4Cwl9DGBPw1sFodruZUPheWVKchlM'
TITLE_START = 39
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
            title = title.string.strip()
            title = title.replace("'", "")
            title = title[TITLE_START:].strip()
            video_titles.append(title)


def output():
    query = "INSERT INTO `buckysroom`.`videos` (`videoID`, `categoryID`, `title`, `code`) VALUES "
    for x, y in enumerate(video_codes):
        query += "\n(NULL, '" + str(CATEGORY) + "', '" + video_titles[x] + "', '" + video_codes[x] + "'),"
    query = query[:-1]
    query += ';'
    print(query)


crawl(PLAYLIST_URL)
output()
