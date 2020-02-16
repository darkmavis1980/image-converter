from PIL import Image
import os
from lib.formats import Formats

def convertImage(source, format, quality = 100):
    path = os.path.split(source)
    filepath = os.path.splitext(path[1])
    source_path = path[0]
    file_name = filepath[0]
    file_extension = filepath[1]
    im = Image.open(source)
    dest_file = "{}/{}.{}".format(source_path, file_name, format)
    print(dest_file)
    im.save(dest_file, format, quality = quality)

    # imagePath = "./images/_DSF344.webp" #example ./test.jpg
    # outputPath = "./images/converted.jpg" #example ./myWebPimage.webp
    # quality = 100 #example 100


    # im = Image.open(imagePath)
    # im.save(outputPath,'jpeg',quality = quality)