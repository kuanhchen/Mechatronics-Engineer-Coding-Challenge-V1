#Title: setup.py 
#Author: Kuan Chen 
#Date: 27/12/2022
#Description: Setup script for making robot_simulation an actual library which is to be published to Pypi
#Pulled from: https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname("D:\DroneDeploy\Mechatronics-Engineer-Coding-Challenge-V1\setup.py"))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="robot_simulation",
    version="0.1.0",
    description="Basic robot simulation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuanhchen/Mechatronics-Engineer-Coding-Challenge-V1",
    author="Kuan Chen",
    author_email="hello@kuanhchen.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["robot_simulation"],
    include_package_data=True,
    install_requires=["deque"]
)