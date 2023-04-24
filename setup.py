from setuptools import setup

setup(
    name="PyCHAS",
    version="0.0.1",
    entry_points={
        'console_scripts':[
            'chas=PyCHAS.chas:chas'
        ]
    },
)