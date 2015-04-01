
from setuptools import setup, find_packages
import sys
import os
sys.path[0:0] = [os.path.join(os.path.abspath(os.path.dirname(__file__)), "src")]


setup(
    name="{{project_name}}",
    version=__import__("{{project_name}}").__version__,
    url='',
    license='',
    description='',
    author='!!AUTHOR!!',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
)
