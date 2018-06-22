from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboDepCheck',
    version='1.0',
    packages=[''],
    package_dir={'': 'robodepcheck'},
    url='https://www.github.com/we45/RoboDepCheck',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for OWASP DEPENDENCY CHECKER' ,
    install_requires=[
        'docker',
        'robotframework==3.0.4'
    ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)

