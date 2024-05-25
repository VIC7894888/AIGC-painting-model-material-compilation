from PIL import Image
import os

def mirror_image(image_path):
    image = Image.open(image_path)
    image_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
    return image_mirror

def batch_mirror_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            mirrored_image = mirror_image(image_path)
            mirrored_image.save(os.path.join(directory, "1" + filename))

# Usage: Provide the correct directory path with escaped backslashes or use raw string literals
batch_mirror_images(r'素材')
