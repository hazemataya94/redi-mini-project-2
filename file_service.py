import os
import sys
import shutil
import csv
import json
from ruamel.yaml import YAML

class FileService:

    def __init__(self):
        self.yaml = YAML()
        self.yaml.width = sys.maxsize
        self.yaml.preserve_quotes = True
        self.yaml.indent(mapping=2, sequence=4, offset=2)
        
    def create_directory(self, path: str):
        os.makedirs(path, exist_ok=True)
    
    def create_directory(self, path: str):
        os.makedirs(path, exist_ok=True)

    def delete_file(self, file_path: str):
        if os.path.exists(file_path):
            os.remove(file_path)
        
    def delete_folder(self, folder_path: str):
        self.delete_directory(folder_path)

    def delete_directory(self, directory_path: str):
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            try:
                shutil.rmtree(directory_path)
            except Exception as e:
                print(f"Error deleting directory {directory_path}: {e}")
        
    def copy_file(self, source: str, destination: str, overwrite: bool):
        if os.path.exists(source) or overwrite:
            shutil.copy2(source, destination)

    def copy_directory(self, source: str, destination: str):
        if os.path.exists(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
    
    def file_exists(self, path):
        return os.path.exists(path)
    
    def folder_exists(self, path):
        return os.path.exists(path)

    def directory_exists(self, path):
        return os.path.exists(path)
        
    def path_exists(self, path):
        return os.path.exists(path)

    def replace_text_in_file(self, source: str, destination: str, old_text: str, new_text: str):
        if os.path.exists(source):
            with open(source, "r", encoding="utf-8") as src, open(destination, "w", encoding="utf-8") as dest:
                content = src.read().replace(old_text, new_text)
                dest.write(content)

    def write_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def read_file(self, file_path):
        if not os.path.exists(file_path):
            exit(1)
        with open(file_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        return content

    def read_yaml_file(self, yaml_path):
        if not os.path.exists(yaml_path):
            exit(1)
        with open(yaml_path, 'r', encoding='utf-8') as file:
            data = self.yaml.load(file)
        return data
    
    def read_json_file(self, json_path):
        if not os.path.exists(json_path):
            exit(1)
        with open(json_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                exit(1)
        return data

    def write_yaml_file(self, yaml_path, data):
        with open(yaml_path, 'w') as file:
            self.yaml.dump(data, file)

    def write_json_file(self, json_path, data):
        with open(json_path, 'w') as file:
            data = json.dumps(data, indent=4)
            file.write(data)

    def append_to_file(self, file_path, content):
        if not os.path.exists(file_path):
            exit(1)
        with open(file_path, 'a', encoding='utf-8') as destination_file:
            destination_file.write(content)

    def prepend_to_file(self, file_path, content):
        if not os.path.exists(file_path):
            exit(1)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content + '\n' + file_content)

    def add_string_after_keyword(self, file_path, keyword, string_to_add='\n'):
        if not os.path.exists(file_path):
            exit(1)
        with open(file_path, 'r+', encoding='utf-8') as file:
            content = file.readlines()
            for i, line in enumerate(content):
                if keyword in line:
                    content.insert(i + 1, string_to_add + '\n')
                    break
            file.seek(0)
            file.writelines(content)
            file.truncate()

    def read_csv_file(self, csv_path):
        if not os.path.exists(csv_path):
            exit(1)
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            clean_data = []
            for row in reader:
                clean_row = {key.strip(): value.strip() for key, value in row.items()}
                clean_data.append(clean_row)
            return clean_data

    def write_csv_file(self, filename, data):
        if not data:
            return
        fieldnames = list(data[0].keys())
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def find_files_with_keyword(self, keyword, directory, return_parent_directory=False):
        matching_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if keyword in file:
                    if return_parent_directory:
                        matching_files.append(os.path.dirname(os.path.join(root, file)))
                    else:
                        matching_files.append(os.path.join(root, file))
        return matching_files

    def get_sorted_subdirectories(self, dir_path, prefix):
        subdirectories = sorted(os.listdir(dir_path))
        return [os.path.join(dir_path, subdir) for subdir in subdirectories
                if subdir.startswith(prefix) and os.path.isdir(os.path.join(dir_path, subdir))]