import os
import shutil
import re

main_directory = ''
destination_folder = 'Merged'

os.makedirs(destination_folder, exist_ok=True)

for i in range(1, 18):
    folder_name = f"CPJ{i}"
    folder_path = os.path.join(main_directory, folder_name)
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".bmp"):
                new_filename = f"{folder_name}_{filename}"
                file_path = os.path.join(folder_path, filename)

                destination_file_path = os.path.join(destination_folder, new_filename)
                shutil.copy(file_path, destination_file_path)

print("Pliki zostały pomyślnie przeniesione i przemianowane!")