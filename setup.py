from setuptools import setup, find_packages

VERSION = '1.0.2'
DESC="Python C/C++ header amalgamation script"

classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX",
    "Operating System :: POSIX :: BSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

kw = {
    "name": "PyCHAS",
    "version": VERSION,
    "description": "Python C/C++ header amalgamation script",
    "long_description": "Python C/C++ header amalgamation script",

    "license": "MIT",
    "author": "NotOkay",
    "author_email": "contact@notokay.dev",
    "url": "https://notokay.dev/",
    "classifiers": classifiers,
    "project_urls": {
        "Source": "https://github.com/EinKara/PyCHAS/",
        "Sponsor": "https://github.com/sponsors/EinKara/"
    },
    "entry_points": {
        "console_scripts":[
            "pychas=PyCHAS.pychas:main"
        ]
    },

    "python_requires": ">=3.7",
    "packages": find_packages(),
}

if __name__ == '__main__':
    setup(**kw)