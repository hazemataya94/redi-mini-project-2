from file_service import FileService

if __name__ == "__main__":
    file_service = FileService()
    
    data_dictionary = file_service.read_csv_file("template.csv")
    print(data_dictionary)