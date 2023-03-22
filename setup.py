"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""

from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='project', # TODO: rename. 
    version=_VERSION,
    description='An empty project base.',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    url='https://github.com/axelmlacap/project',  # TODO.
    download_url='https://github.com/axelmlacap/project/tarball/{}'.format(_VERSION),  # TODO.
    author='Axel Lacapmesure',  # TODO.
    author_email='alacapmesure@fi.uba.ar',  # TODO.
    packages=find_packages(where='project'),  # TODO.
    package_dir={"": "project"},
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=["numpy", "tifffile"],
    include_package_data=True,
    license='TODO',  # TODO: set your license string. 
    keywords='empty project TODO keywords'
)

