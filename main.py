import json
from file_service import FileService

csv_file_path = "template.csv"

if __name__ == "__main__":
    
    file_service = FileService()
    data_dictionary = file_service.read_csv_file(csv_file_path)
    print(json.dumps(data_dictionary, indent=4))
