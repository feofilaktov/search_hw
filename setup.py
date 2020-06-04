import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='search_hw',
    version='0.1',
    # packages=find_packages(),
    packages=['search_hw'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Genereates random number',
    long_description=README,
    # url='https://github.com/...',
    author='ripperzx',
    author_email='feofilaktov@gmail.com',
    keywords=['google', 'parser'],
    # classifiers=[],
    # install_requires=[
    #     "Django >= 2.0",
    # ],
)
