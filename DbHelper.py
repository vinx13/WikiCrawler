import sqlite3

from tools import singleton


@singleton
class DbHelper(object):
    """
        Encapsulate basic operations of database
    """
    DB_FILENAME = "../res/data.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_FILENAME)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.commit()
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()

    def getResult(self, count=0):
        """
            :param count: number of results to fetch, 0 to fetch all
        """
        if count == 0:
            return self.cursor.fetchall()
        return self.cursor.fetchmany(count)
