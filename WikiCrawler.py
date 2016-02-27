from time import sleep

from CatagoryManager import CatagoryManager
from EntryManager import EntryManager
from HtmlParser import HtmlParser
from HtmlReader import HtmlReader
from Logger import Logger
from QueueProxy import QueueProxy


class WikiCrawler(object):
    TAG = "WikiCrawler"

    def __init__(self):
        self.queue = QueueProxy()
        self.entryMgr = EntryManager()
        self.catagoryMgr = CatagoryManager()
        self.logger = Logger()

    def run(self):
        while True:
            try:
                sleep(1)
                url = self.queue.pop()
                html = HtmlReader(url).read()
                entry = HtmlParser(html, url).parse()
                for child in entry.children:
                    if not self.entryMgr.contains(child):
                        self.queue.push(child)
                self.entryMgr.add(entry)
                self.catagoryMgr.add(entry)
            except Exception, e:
                self.logger.e(self.TAG, e.message)
