import os
import shutil
from datetime import datetime, timedelta

def list_files(PATH):
    return [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]

def is_recently_modified(file_path):
    file_stats = os.stat(file_path)
    current_time = datetime.now()
    time_difference = current_time - datetime.fromtimestamp(file_stats.st_mtime)
    return time_difference < timedelta(days=1)

def create_last_24hours_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def update_file_content(file_path):
    with open(file_path, 'a') as file:
        file.write(f'\nUpdated at {datetime.now()}')

def move_file_to_last_24hours(file_path, destination_folder):
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def main():
    web_folder = 'web'
    last_24hours_folder = os.path.join(web_folder, 'last_24hours')  

    files = list_files(web_folder)

    for file in files:
        file_path = os.path.join(web_folder, file)
        if is_recently_modified(file_path):
            update_file_content(file_path)
            create_last_24hours_folder(last_24hours_folder)
            move_file_to_last_24hours(file_path, last_24hours_folder)

if __name__ == "__main__":
    main()
