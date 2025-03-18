import os

folder_path = 'DatasetMerged'
bmp_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]
bmp_files.sort()

for i, old_name in enumerate(bmp_files, start=1):
    old_path = os.path.join(folder_path, old_name)
    new_name = f'plikMERGED{i}.bmp'
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Nazwy plików zostały zmienione.")