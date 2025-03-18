import os
from PIL import Image
import numpy as np

input_folder = "Merged"
output_folder = "dataset_binarized2"


def binarize_image(image_path, threshold=45):
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    row, col = image_array.shape
    for x in range(row):
        for y in range(col):
            if image_array[x][y] < threshold:
                image_array[x][y] = 0
            else:
                image_array[x][y] = 255
    return Image.fromarray(image_array.astype(np.uint8))


os.makedirs(output_folder, exist_ok=True)

sorted_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".bmp")],
                      key=lambda f: int(f.split('plik')[1].split('.bmp')[0]))

for filename in sorted_files:
    source_file = os.path.join(input_folder, filename)
    binary_image = binarize_image(source_file)
    destination_file = os.path.join(output_folder, filename)  # Używamy tej samej nazwy pliku
    binary_image.save(destination_file)

print(f"Pliki zostały pomyślnie zbinaryzowane i zapisane w folderze {output_folder}.")