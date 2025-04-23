from database_training.sqlite_connect import RediSQLiteConnection
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    db_path = "redi.db"

    logging.info("Connecting to the database 'redi.db'")
    redi_db = RediSQLiteConnection(db_path)
    
    ### Run Your Code Here
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###

    logging.info("Closing the database connection")
    redi_db.close()
