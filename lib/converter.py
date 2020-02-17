from PIL import Image
from lib.formats import Formats
import os

class FormatException(Exception):
    """Format not recognized"""
    pass

def convertImage(source, file_format, quality = 100):
    try:
        path = os.path.split(source)
        filepath = os.path.splitext(path[1])
        source_path = path[0]
        file_name = filepath[0]
        file_extension = filepath[1][1:]
        if Formats[file_format.upper()] is None:
            raise KeyError
        dest_extension = Formats[file_format.upper()].value
        print(dest_extension, file_extension)
        if dest_extension == file_extension:
            raise Exception('Same extension, please choose another format')
        print(file_format)
        dest_file = "{}/{}.{}".format(source_path, file_name, dest_extension)
        print(dest_file)
        if os.path.exists(dest_file):
            raise Exception('File {} already exists'.format(dest_file))
        im = Image.open(source)
        im.save(dest_file, format, quality = quality)
    except KeyError as error:
        print('File format not recognized')
    except Exception as error:
        print(error)
    finally:
        print("All done!")
