import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vkmount",
    version = "0.0.1",
    author = "radmir agliullin",
    author_email = "pr3xis@ya.ru",
    description = (""),
    license = "",
    keywords = "vk.com vkontakte vk fuse",
    url = "https://github.com/last1k/vkmount",
    packages=['vkmount', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        #"Topic :: Utilities",
        #"License :: OSI Approved :: BSD License",
        ],
)