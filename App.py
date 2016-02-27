from EntryManager import EntryManager
from Logger import Logger
from QueueProxy import QueueProxy
from WikiCrawler import WikiCrawler


class App(object):
    TAG = "App"

    def __init__(self, *startUrls):
        self.crawler = WikiCrawler()
        self.logger = Logger()
        queue = QueueProxy()
        entryMgr = EntryManager()
        for url in filter(lambda url: not entryMgr.contains(url), startUrls):
            queue.push(url)

    def run(self):
        self.logger.i(self.TAG, "Crawler started.")
        self.crawler.run()
