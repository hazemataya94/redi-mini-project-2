import sqlite3

class RediSQLiteConnection:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS car (id INTEGER PRIMARY KEY AUTOINCREMENT, brand TEXT, color TEXT)")
        self.conn.commit()

    def insert_data(self):
        self.cursor.execute("INSERT INTO car (brand, color) VALUES ('Toyota', 'Red')")
        self.conn.commit()

    def select_data(self):
        self.cursor.execute("SELECT * FROM car")
        return self.cursor.fetchall()
    
    def update_data(self):
        self.cursor.execute("UPDATE car SET color = 'Blue' WHERE brand = 'Toyota'")
        self.conn.commit()

    def delete_data(self):
        self.cursor.execute("DELETE FROM car WHERE brand = 'Toyota'")
        self.conn.commit()