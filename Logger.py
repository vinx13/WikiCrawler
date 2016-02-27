from datetime import datetime

from tools import singleton


@singleton
class Logger(object):
    def d(self, tag, message):
        print self.format("DEBUG", tag, message)

    def e(self, tag, message):
        print self.format("ERROR", tag, message)

    def i(self, tag, message):
        print self.format("INFO", tag, message)

    def format(self, level, tag, message):
        return level + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + tag + " " + message
