from database_training.sqlite_connect import RediSQLiteConnection
import logging
if __name__ == "__main__":
    db_path = "redi.db"
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Connecting to the database 'redi.db'")
    redi_db = RediSQLiteConnection(db_path)
    redi_db.create_table()
    logging.info("Closing the database connection")
    redi_db.close()
