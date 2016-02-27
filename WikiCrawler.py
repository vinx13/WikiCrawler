from CatagoryManager import CatagoryManager
from EntryManager import EntryManager
from HtmlParser import HtmlParser
from HtmlReader import HtmlReader
from QueueProxy import QueueProxy


class WikiCrawler(object):
    def __init__(self):
        self.queue = QueueProxy()
        self.entryMgr = EntryManager()
        self.catagoryMgr = CatagoryManager()

    def run(self):
        while True:
            url = self.queue.pop()
            html = HtmlReader(url).read()
            entry = HtmlParser(html, url).parse()
            for child in entry.children:
                self.queue.push(child)
            self.entryMgr.add(entry)
            self.catagoryMgr.add(entry)
