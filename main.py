from database_training.sqlite_connect import RediSQLiteConnection
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    db_path = "redi.db"

    logging.info("Connecting to the database 'redi.db'")
    
    redi_db = RediSQLiteConnection(db_path)
    input("1- Press Enter to continue...")
    
    table_name = "car"
    redi_db.drop_table(table_name)
    print(f"redi_db.create_table({table_name})")
    redi_db.create_table(table_name)
    input("2- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Toyota', 'White')")
    redi_db.insert_data(table_name, "Toyota", "White")
    input("3- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Toyota', 'Silver')")
    redi_db.insert_data(table_name, "Toyota", "Silver")
    input("4- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Mazda', 'Red')")
    redi_db.insert_data(table_name, "Mazda", "Red")
    input("5- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Mazda', 'Blue')")
    redi_db.insert_data(table_name, "Mazda", "Blue")
    input("6- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Honda', 'Yellow')")
    redi_db.insert_data(table_name, "Honda", "Yellow")
    input("7- Press Enter to continue...")
    print(f"redi_db.insert_data({table_name}, 'Honda', 'Green')")
    redi_db.insert_data(table_name, "Honda", "Green")
    input("8- Press Enter to continue...")
    print(f"redi_db.select_data({table_name})")
    print(redi_db.select_data(table_name))
    input("9- Press Enter to continue...")
    print(f"redi_db.update_color_where_brand({table_name}, 'Toyota', 'Black')")
    redi_db.update_color_where_brand(table_name, "Toyota", "Black")
    input("10- Press Enter to continue...")
    print(f"redi_db.delete_data_color({table_name}, 'Yellow')")
    redi_db.delete_data_color(table_name, "Yellow")
    input("11- Press Enter to continue...")
    print(f"redi_db.delete_data_id({table_name}, 2)")
    redi_db.delete_data_id(table_name, 2)
    input("12- Press Enter to continue...")
    print(f"redi_db.drop_table({table_name})")
    redi_db.drop_table(table_name)
    input("13- Press Enter to continue...")
    
    logging.info("Closing the database connection")
    redi_db.close()
