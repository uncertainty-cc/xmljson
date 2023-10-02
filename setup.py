#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with io.open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='xmljson',
    version='0.2.1',
    description='Converts XML into JSON/Python dicts/arrays and vice-versa.',
    long_description=readme + '\n\n' + history,
    author='S Anand',
    author_email='root.node@gmail.com',
    url='https://github.com/sanand0/xmljson',
    packages=[
        'xmljson',
    ],
    package_dir={'xmljson':
                 'xmljson'},
    include_package_data=True,
    install_requires=[],
    license='MIT',
    zip_safe=False,
    keywords='xmljson',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',    # For collections.Counter
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
    tests_require=['lxml'],
    entry_points={
        'console_scripts': [
            'xml2json = xmljson.__main__:main'
        ]
    }
)
