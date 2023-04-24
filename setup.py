from setuptools import setup

VERSION = '0.0.1'
DESC="Python C/C++ header amalgamation script"

setup(
    name="PyCHAS",
    version=VERSION,
    description=DESC,
    long_description=DESC,
    author="NotOkay",
    author_email="contact@notokay.dev",
    license='MIT',
    entry_points={
        'console_scripts':[
            'chas=PyCHAS.chas:entry'
        ]
    },
)