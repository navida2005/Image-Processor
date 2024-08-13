from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./raw_images"  # Input directory
pathOut = "./edited_images"  # Output directory

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

for file in os.listdir(path):
    if file.endswith(valid_extensions):  # Process only valid image files
        img = Image.open(f"{path}/{file}")
        edit = img.convert("L").filter(ImageFilter.DETAIL).filter(ImageFilter.SHARPEN)
        edit = ImageEnhance.Contrast(edit).enhance(1)  # Adjust contrast
        edit.save(f"{pathOut}/{os.path.splitext(file)[0]}_edited.jpg")
