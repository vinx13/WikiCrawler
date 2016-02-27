from DbHelper import DbHelper
from tools import checkDB

class CatagoryManager(object):
    TABLE_NAME = "catagory"
    FIELD_TITLE = "title"
    FIELD_COUNT = "count"

    def __init__(self):
        self.db = DbHelper()
        sql = "CREATE TABLE IF NOT EXISTS `" + self.TABLE_NAME + "` (" \
              + self.FIELD_TITLE + " TEXT NOT NULL," \
              + self.FIELD_COUNT + " INT NOT NULL DEFAULT '1'," \
              + "PRIMARY KEY (`" + self.FIELD_TITLE + "`(100)));"

        self.db.execute(sql)
    @checkDB
    def add(self, entry):
        for title in entry.catagories:
            sql = "INSERT INTO `" + self.TABLE_NAME + "` VALUES ('" \
                  + title + "', 1) " \
                  + "ON DUPLICATE KEY UPDATE " + self.FIELD_COUNT + " = " + self.FIELD_COUNT + " + 1;"
            self.db.execute(sql)
    @checkDB
    def clear(self):
        sql = "DELETE FROM " + self.TABLE_NAME + ";"
        self.db.execute(sql)
