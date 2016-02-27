import MySQLdb

from Config import Config
from tools import singleton


@singleton
class DbHelper(object):
    """
        Encapsulate basic operations of database
    """

    def __init__(self):
        self.conn = MySQLdb.connect(
            host=Config.HOST,
            port=Config.PORT,
            user=Config.USER,
            passwd=Config.PASSWORD,
            db=Config.DB_NAME
        )
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        self.cursor.execute(sql)

    def getResult(self, count=0):
        """
            :param count: number of results to fetch, 0 to fetch all
        """
        if count == 0:
            return self.cursor.fetchall()
        return self.cursor.fetchmany(count)
DbHelper()