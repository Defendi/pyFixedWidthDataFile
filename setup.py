# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pyFixedWidthDataFile',
    version='0.0.1',
    author='OpusSystem',
    author_email='suporte@opussystem.com.br',
    url='https://www.opussystem.com.br',
    keywords=['fixed', 'width', 'text'],
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    package_data={
    },
    install_requires=[
        'setuptools-git',
    ],
    license='MIT',
    description='This is a simple library for creating fixed-width text files for transferring data between APIs.',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/Defendi/pyFixedWidthDataFile',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    tests_require=[
    ],
)
