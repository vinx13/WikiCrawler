import bs4

from Entry import Entry


class HtmlParser(object):
    def __init__(self, html, url):
        self.html = html
        self.url = url

    def parse(self):
        soup = bs4.BeautifulSoup(self.html, "lxml")
        mainContent = soup.find(id='mw-content-text')
        catagoryContent = soup.find(id="mw-normal-catlinks")

        title = soup.find(id='firstHeading').contents[0]

        children = filter(lambda url: url.startswith("/wiki") and ':' not in url,
                          map(lambda tag: (tag['href']),
                              mainContent.find_all('a')))

        if catagoryContent:
            catagories = map(lambda aTag: aTag['title'].lstrip("Category:"),
                             filter(lambda aTag: (aTag['href'].startswith('/wiki/Category:')),
                                    catagoryContent.find_all('a')))

        if catagories is None:
            catagories = []

        return Entry(self.url, title, children, catagories)
