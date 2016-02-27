from QueueProxy import QueueProxy
from WikiCrawler import WikiCrawler


class App(object):
    def __init__(self, *startUrls):
        self.crawler = WikiCrawler()
        queue = QueueProxy()
        for url in startUrls:
            queue.push(url)

    def run(self):
        self.crawler.run()
