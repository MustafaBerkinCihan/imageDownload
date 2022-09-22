
from pathlib import Path
from PIL import Image
import os
#os.mkdir("fotolar\webpcnvrt")
def convert_to_webp(fotolar):

    destination = fotolar.with_suffix(".webp")

    image = Image.open(fotolar)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    paths = Path("fotolar").glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)


main()