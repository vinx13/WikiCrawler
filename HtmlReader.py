import urllib2


class HtmlReader(object):
    URL_BASE = "https://en.wikipedia.org"

    def __init__(self, url):
        self.url = self.URL_BASE + url

    def read(self):
        request = urllib2.Request(self.url)
        return urllib2.urlopen(request).read()