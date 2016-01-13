#!/usr/bin/python
# Filename: setup.py


import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name="bovespaparser",
      version="0.6.4",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      package_data={'': ['*.md', '*.txt']},
      include_package_data=True,
      author="Roberto Haddock Lobo",
      author_email="rhlobo+stockexperiments@gmail.com",
      description="Bovespa's historical series files parser.",
      long_description=read('README.md'),
      license="MIT",
      test_suite='bovespaparser.tests.bovespaparser_tests.TestBovespaParserFunctions',
      url='http://pypi.python.org/pypi/bovespaparser',
      keywords=["bovespa", "parser", "historical", "series", "cotahist", "stock"],
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 2.7",
                   "Development Status :: 4 - Beta",
                   "Environment :: Other Environment",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Financial and Insurance Industry",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: Office/Business :: Financial :: Investment"])
