#!/usr/bin/env python
from setuptools import setup, find_packages
import sys
import os

version = "1.0.0"

with open("README.md", "r") as f:
    long_description = f.read()

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="DRV8870",
    version=version,
    author="Rodney Osodo",
    author_email="blackd0t@protonmail.com",
    description="Pure Python library for reading DHT11 sensor on Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["RPi.GPIO"],
    python_requires=">=3.6",
    license="GNU GENERAL PUBLIC LICENSE",
    url="https://github.com/0x6flab/satima-arduinolibrary/tree/main/raspberrypi",
    download_url="http://pypi.python.org/pypi/DRV8870/",
    zip_safe=True,
    py_modules=[],
    keywords="pysendyit sendy wrapper api",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
