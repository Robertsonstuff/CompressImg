from PIL import Image
import PIL
import os
import glob

subdirectory = 'C:/full/file/path'

a = input("I need the full file path on where to compress? ")

def compress_images(directory=False, quality=30):
    # from current directory
    if directory:
        os.chdir(directory)
    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()
    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('jpg', 'png'))]
    # 4. Loop over every image:
    for image in images:
        print(f"Compressing {image} now...")
        # 5. Open every image:
        img = Image.open(image)
        # 6. Resize image to 800x800
        b = (800, 800)
        size_image = img.thumbnail(b)
        # 7. Compress every image and save it with a new name:
        img.save("Compressed-"+image, optimize=True, quality=quality)

compress_images(directory=subdirectory)
