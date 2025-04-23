import sqlite3

class RediSQLiteConnection:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self, table_name):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, brand TEXT, color TEXT)")
        self.conn.commit()

    def insert_data(self, table_name, brand, color):
        self.cursor.execute(f"INSERT INTO {table_name} (brand, color) VALUES ('{brand}', '{color}')")
        self.conn.commit()

    def select_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()
    
    def update_color_where_brand(self, table_name, brand, color):
        self.cursor.execute(f"UPDATE {table_name} SET color = '{color}' WHERE brand = '{brand}'")
        self.conn.commit()
        
    def update_brand_where_color(self, table_name, color, brand):
        self.cursor.execute(f"UPDATE {table_name} SET brand = '{brand}' WHERE color = '{color}'")
        self.conn.commit()

    def delete_data_brand(self, table_name, brand):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE brand = '{brand}'")
        self.conn.commit()
        
    def delete_data_color(self, table_name, color):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE color = '{color}'")
        self.conn.commit()
    
    def delete_data_id(self, table_name, id):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE id = '{id}'")
        self.conn.commit()
        
    def delete_all_data(self, table_name):
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.conn.commit()

    def drop_table(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()