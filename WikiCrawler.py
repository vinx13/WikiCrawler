class WikiCrawler(object):
    def __init__(self):
        self.queue = QueueProxy()
        self.entryMgr = EntryManager()
    def run(self):
        while True:
            url = self.queue.pop()
            html = HtmlReader(url).read()
            entry = HtmlParser(html)
            for child in entry.children:
                self.queue.push(child)
            self.entryMgr.add(entry)


