from setuptools import setup

setup(
    name="PyCHAS",
    version="0.0.1",
    description="Python C/C++ header amalgamation script",
    entry_points={
        'console_scripts':[
            'chas=PyCHAS.chas:entry'
        ]
    },
)