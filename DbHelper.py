import MySQLdb

from Config import Config
from Logger import Logger
from tools import singleton


@singleton
class DbHelper(object):
    """
        Encapsulate basic operations of database
    """
    TAG = "DbHelper"

    def __init__(self):
        self.connect()
        self.logger = Logger()

    def connect(self):
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
        try:
            self.conn.ping()
        except Exception:
            self.connect()
            self.logger.i(self.TAG, "Mysql reconnected.")

        self.connect()
        self.cursor.execute(sql)

    def getResult(self, count=0):
        """
            :param count: number of results to fetch, 0 to fetch all
        """
        if count == 0:
            return self.cursor.fetchall()
        return self.cursor.fetchmany(count)
