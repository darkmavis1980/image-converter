from lib.converter import convertImage
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images from and to webp")
    parser.add_argument('--source', '-s', dest="source", metavar="-s", type=str, help="Image source")
    parser.add_argument('--format', '-f', dest="format", type=str, help="Format to convert to", default="web")
    parser.add_argument('--quality', '-q', dest="quality", type=int, help="Image quality (0-100) range", default=100)
    args = parser.parse_args()
    convertImage(args.source, args.format, args.quality)
