import logging
import sqlite3


class SQLiteHandler(logging.Handler):
    def __init__(self, db_path):
        logging.Handler.__init__(self)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            levelname TEXT,
            message TEXT,
            created FLOAT
        )
        """)

    def emit(self, record):
        self.cursor.execute("""
        INSERT INTO logs (levelname, message, created) VALUES (?, ?, ?)
        """, (record.levelname, record.msg, record.created))
        self.conn.commit()


logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

db_handler = SQLiteHandler('logs.db')
logger.addHandler(db_handler)

logger.info("This log message will be saved in the SQLite database")
