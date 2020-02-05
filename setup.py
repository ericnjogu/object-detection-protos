import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name = "juu-object-detection-protos",
    version = "0.1",
    author = "Eric Njogu",
    author_email = "kunadawa@gmail.com",
    description = "holds the protobuf files for the protobuf messages that are exchanged between the various services",
    license = "MIT",
    keywords = "protobuf tensorflow",
    url = "https://github.com/kunadawa/object-detection-protos",
    packages = find_packages(),
    long_description = read('readme.md'),
    classifiers = [
        "Development Status :: active",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
