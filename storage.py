import shutil
import os
from config import IMAGES_DIR
from id_generator import generate_id

def save_image(source_path):
    os.makedirs(IMAGES_DIR, exist_ok=True)
    image_id = generate_id()
    extension = os.path.splitext(source_path)[1]
    dest_path = os.path.join(IMAGES_DIR, image_id + extension)
    shutil.copy(source_path, dest_path)
    return image_id
    

def get_image(image_id):
    for filename in os.listdir(IMAGES_DIR):
        if filename.startswith(image_id):
            return os.path.join (IMAGES_DIR, filename)
    return None

