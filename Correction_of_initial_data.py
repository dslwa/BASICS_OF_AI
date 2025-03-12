from PIL import Image
import os


def crop_top_bottom(image_path, output_path, pixels):
    img = Image.open(image_path)
    width, height = img.size
    img_cropped = img.crop((0, pixels, width, height - pixels))
    img_cropped.save(output_path)


def process_images_in_folders(base_folder):
    for folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder)

        if os.path.isdir(folder_path):
            output_folder = f"{folder_path}_result"
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for filename in os.listdir(folder_path):
                if filename.lower().endswith('.bmp'):
                    input_path = os.path.join(folder_path, filename)
                    output_path = os.path.join(output_folder, filename)
                    crop_top_bottom(input_path, output_path, pixels=30)
