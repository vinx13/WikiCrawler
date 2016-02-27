class Entry(object):
    def __init__(self, url, title, children, catagories):
        self.title = title
        self.url = url
        self.children = children
        self.catagories = catagories

    def __hash__(self):
        return self.url.hash()