#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('PYPI_LONG_DESCRIPTION.rst') as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = [req.strip() for req in f.readlines()]

test_requirements = [
    "nose",
    "coverage",
    "pycallgraph",
    "mock"
]


setup(
    name='xlseries',
    version='0.1.13',
    description="Python package to scrape time series data from excel files.",
    long_description=readme,
    author="Agustin Benassi",
    author_email='agusbenassi@gmail.com',
    maintainer="Agustin Benassi",
    maintainer_email='agusbenassi@gmail.com',
    url='https://github.com/abenassi/xlseries',
    download_url='https://github.com/abenassi/xlseries/archive/master.zip',
    packages=[
        'xlseries',
        'xlseries.strategies',
        'xlseries.strategies.clean',
        'xlseries.strategies.discover',
        'xlseries.strategies.get',
        'xlseries.utils'
    ],
    package_dir={'xlseries': 'xlseries'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3+",
    zip_safe=False,
    keywords="xlseries excel time series data opendata scraper",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business'
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
