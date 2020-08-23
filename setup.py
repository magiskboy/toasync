from setuptools import setup

with open('./README.md', 'r') as fi:
    readme = fi.read()

setup(
    name='toasync',
    version='0.0.1',
    author='Nguyen Khac Thanh',
    packages=['toasync'],
    long_description=readme
)
