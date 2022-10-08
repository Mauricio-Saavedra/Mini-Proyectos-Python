from distutils import extension
from PIL import Image
import os

downloadsfolder = r"Users\52554\Downloads"

if __name__ == "__main__":
    for filename in os.listdir(downloadsfolder):
        name, extension = os.path.splitext(downloadsfolder + filename)

        if extension in [".jpg", "jpeg", "png"]:
            picture = Image.open(downloadsfolder + filename)
            picture.save(downloadsfolder + "compressed_"+filename, optimize=True, quality=60)
