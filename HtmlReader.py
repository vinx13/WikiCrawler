import urllib2

from Logger import Logger


class HtmlReader(object):
    TAG = "HtmlReader"
    URL_BASE = "https://en.wikipedia.org"

    def __init__(self, url):
        self.url = self.URL_BASE + url
        self.logger = Logger()

    def read(self):
        self.logger.i(self.TAG, " Visiting url " + self.url)
        request = urllib2.Request(self.url)
        return urllib2.urlopen(request).read()
