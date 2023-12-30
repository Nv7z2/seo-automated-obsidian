import os
import json

def read_config_json(project_name: str):
    full_config_file_path = f'configs/{project_name}.json'

    with open(full_config_file_path, 'r') as config_file:
        return json.load(config_file)

def list_all_md_files(directory: str, excluded_directories=None):
    md_files = []
    exclude_dirs = set(os.path.join(directory, d) for d in excluded_directories) if excluded_directories else set()

    for root, directories, files in os.walk(directory):
        directories[:] = [directory for directory in directories if os.path.join(root, directory) not in exclude_dirs]

        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    return md_files

def read_file_content(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('file not found')

def extract_file_meta_info(file_path: str):
    content = read_file_content(file_path)
    start, end = content.find('---'), content.find('---', 3)

    if start != -1 and end != -1:
        return content[start + 3:end].strip()
    else:
        return f"Meta info not found in this file: {file_path}."

def get_file_meta_dict(file_path: str):
    file_meta = extract_file_meta_info(file_path)
    file_meta_dict = {}

    for line in file_meta.split('\n'):
        line_splitted = line.split(':', 1)
        file_meta_dict[line_splitted[0]] = line_splitted[1].strip()
    
    return file_meta_dict
