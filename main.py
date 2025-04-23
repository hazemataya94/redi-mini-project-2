from database_training.sqlite_connect import RediSQLiteConnection
from database_training.sqlite_orm import session, Student

import logging
logging.basicConfig(level=logging.DEBUG)

def sqlite_connect():
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

def sqlite_orm():
    
    input("1- Press Enter to continue...")
    logging.info("Adding a new student")
    
    student = Student(first_name="John", last_name="Doe")
    
    print("student id:")
    student.print_id()
    
    session.add(student)
    session.commit()
    
    print("student id:")
    student.print_id()
    
    input("2- Press Enter to continue...")
    print("Querying all students")
    students = session.query(Student).all()
    for student in students:
        student.print_all()
    
    input("3- Press Enter to continue...")
    logging.info("Adding a new student")
    session.add(Student(first_name="Jane", last_name="Dow"))
    session.commit()

    input("4- Press Enter to continue...")
    print("Querying all students")
    students = session.query(Student).all()
    for student in students:
        student.print_all()
    
    
if __name__ == "__main__":
    
    # sqlite_connect()
    
    sqlite_orm()
    
