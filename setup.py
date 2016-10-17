#!/user/bin/env python
from distutils.core import setup
#from setuptools import setup

setup(
    name = "littlepy",
    description = "Provide python utility in linux pipe, takes commands from stdin and parse into pandas dataframe variable X",
    author = "Shawn Chen",
    author_email = "chen.xiaoc89@gmail.com",
    license = "MIT",
    version = "0.99",    
    url="git@github.com:cxccxlcxc/littlepy.git",
    packages = ["littlepy"],
    scripts = ["scripts/py"],
    data_files = [("data", ["data/test.csv"])]
)