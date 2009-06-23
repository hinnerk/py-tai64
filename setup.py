import os
from setuptools import setup, find_packages

def read(fname):
    """ returns string from file 'fname' located in the same
        directory as setup.py."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tai64n",
    version = "0.3.3",
    url = 'http://bitbucket.org/hinnerk/py-tai64n/',
    license = 'BSD',
    description = "Converts TAI64(n) string to datetime.datetime (UTC) object.",
    long_description = read('README'),

    author = 'Hinnerk Haardt',
    author_email = 'hinnerk@randnotizen.de',

    packages = ['tai64n'],
    
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Other/Nonlisted Topic',
    ]
)
