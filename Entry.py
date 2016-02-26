class Entry(object):
    def __init__(self, title, url, catagories):
        self.title = title
        self.url = url
        self.catagories = catagories

    def __hash__(self):
        return self.url.hash()