#! /usr/bin/env python3

from PIL import Image
from enum import Enum
import os
import argparse

class Formats(Enum):
    jpg = 'jpg'
    jpeg = 'jpg'
    png = 'png'
    webp = 'webp'

def convertImage(source, file_format, quality = 100):
    try:
        path = os.path.split(source)
        filepath = os.path.splitext(path[1])
        print("Converting {image} to {file_format}".format(image=path[1], file_format=file_format))
        source_path = path[0]
        file_name = filepath[0]
        file_extension = filepath[1][1:]
        if Formats[file_format] is None:
            raise KeyError
        dest_extension = Formats[file_format].value
        if dest_extension == file_extension:
            raise Exception('Same extension, please choose another format')
        dest_file = "{}/{}.{}".format(source_path, file_name, dest_extension)
        if os.path.exists(dest_file):
            raise Exception('File {} already exists'.format(dest_file))
        im = Image.open(source)
        im.save(dest_file, file_format, quality = quality)
    except KeyError as error:
        print('File format not recognized')
    except Exception as error:
        print(error)
    else:
        print("Your image has been converted to {file_format}!".format(file_format=file_format))

def initConvert():
    parser = argparse.ArgumentParser(description="Convert images from and to webp")
    parser.add_argument('--source', '-s', dest="source", metavar="-s", type=str, help="Image source")
    parser.add_argument('--format', '-f', dest="format", type=str, help="Format to convert to", default="web")
    parser.add_argument('--quality', '-q', dest="quality", type=int, help="Image quality (0-100) range", default=100)
    args = parser.parse_args()
    convertImage(args.source, args.format, args.quality)

if __name__ == "__main__":
    initConvert()