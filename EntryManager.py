"""
    deal with basic CURD for words"
"""
from DbHelper import DbHelper


class EntryManager:
    TABLE_NAME = "entry"
    FIELD_TITLE = "title"
    FIELD_URL = "url"
    FIELD_COUNT = "count"

    def __init__(self):
        self.db = DbHelper()
        sql = "CREATE TABLE IF NOT EXISTS `" + self.TABLE_NAME + "` (" \
              + self.FIELD_URL + " TEXT NOT NULL," \
              + self.FIELD_TITLE + " TEXT NOT NULL," \
              + self.FIELD_COUNT + " INT NOT NULL DEFAULT '1'," \
              + "PRIMARY KEY (`" + self.FIELD_URL + "`(100)));"

        self.db.execute(sql)

    def add(self, entry):
        sql = "INSERT INTO `" + self.TABLE_NAME + "` VALUES ('" \
              + entry.url + "', '" + entry.title + "', 1);"
        self.db.execute(sql)

    def update(self, url):
        sql = "UPDATE " + self.TABLE_NAME + " SET " \
              + self.FIELD_COUNT + " = " + self.FIELD_COUNT + " + 1 WHERE " + self.FIELD_URL + " = '" + url + "';"
        self.db.execute(sql)

    def clear(self):
        sql = "DELETE FROM " + self.TABLE_NAME + ";"
        self.db.execute(sql)

    def contains(self, url):
        sql = "SELECT * FROM `" + self.TABLE_NAME + "` WHERE " + self.FIELD_URL + " = '" + url + "';"
        self.db.execute(sql)
        rows = self.db.getResult()
        return len(rows) > 0
