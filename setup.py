# setup.py
from setuptools import setup, find_packages

setup(
    name='DataPrepKit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A comprehensive toolkit for preprocessing datasets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
