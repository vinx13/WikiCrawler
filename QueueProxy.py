from DbHelper import DbHelper
from tools import singleton


@singleton
class QueueProxy(object):
    TABLE_NAME = "queue"
    FIELD_URL = "url"
    FIELD_ID = "id"

    def __init__(self):
        self.db = DbHelper()
        sql = "CREATE TABLE IF NOT EXISTS `" + self.TABLE_NAME \
              + "` (" + self.FIELD_URL + " TEXT NOT NULL, " \
              + self.FIELD_ID + " INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`" + self.FIELD_ID + "`));"
        self.db.execute(sql)

    def push(self, url):
        sql = "INSERT INTO " + self.TABLE_NAME + " (" + self.FIELD_URL + ") VALUES ('" + url + "');"
        self.db.execute(sql)

    def pop(self):
        sql = "SELECT " + self.FIELD_URL + ", " + self.FIELD_ID + " FROM " + self.TABLE_NAME + " ORDER BY " + self.FIELD_ID + " LIMIT 1;"
        self.db.execute(sql)
        row = self.db.getResult()[0]
        url, id = row
        sql = "DELETE FROM " + self.TABLE_NAME + " WHERE " + self.FIELD_ID + " = " + str(id) + ";"
        self.db.execute(sql)
        return url

    def clear(self):
        sql = "DELETE FROM " + self.TABLE_NAME + ";"
        self.db.execute(sql)
