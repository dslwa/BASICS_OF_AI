from PIL import Image
import os

folder_path = 'Merged'
bmp_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]
for file in bmp_files:
    file_path = os.path.join(folder_path, file)
    with Image.open(file_path) as img:
        width, height = img.size
        new_img = img.crop((0, 30, width, height - 30))
        new_file_path = os.path.join(folder_path, f'cropped_{file}')
        new_img.save(new_file_path)

print("Obrazy zostały przycięte.")