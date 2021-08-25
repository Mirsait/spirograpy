""" Converting .eps to .png """

from glob import glob
from wand.image import Image


def convert_eps_to_png():
    """ converting .eps to .png from images/ """
    # list of eps files in current folder
    files = glob('images/*.eps')
    for file in files:
        print(file)
        # Read .eps image using Image() function
        with Image(filename=f"{file}") as img:
            # Change format in python using format property
            img.format = 'jpeg'
            # Save final image
            img.save(filename=f"PNG24:{file}.png")
