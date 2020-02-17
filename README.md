# Webp Converter

This is a simple Python project to convert images from and to Google's WebP file format, and it's written in Python 3.

## Install dependencies

**Install it with Pip**

```bash
# Create the env
virtualenv env

# Activate the virtualenv
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Or **use pipenv**

```bash
# Install dependencies and create env
pipenv install -r requirements.txt

# Activate the virtualenv
pipenv shell
```

## Usage

```bash
# This will convert a jpg image to a WebP
python3 webpConverter --source /path/to/my/image.jpg --format webp

# Shorter format
python3 webpConverter -s /path/to/my/image.jpg -f webp
```

By default it will convert to the maximum image quality (max = 100), but if you want to lower it down to reduce the filesize you can provide a `--quality [N]` flag:

```bash
# This will convert a jpg image to a WebP
python3 webpConverter --source /path/to/my/image.jpg --format webp --quality 60
```

## Build the project

```bash
# Runt he setup.py script
python3 setup.py sdist bdist_wheel

# Install it locally
pip install .

# or with live changes
pip install -e .
```

## More info on how to package a python project

- [python-packaging](https://python-packaging.readthedocs.io/en/latest/minimal.html)