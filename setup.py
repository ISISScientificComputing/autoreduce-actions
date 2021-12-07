# pylint:skip-file
"""
Wrapper for the functionality for various installation and project setup commands
see:
    `python setup.py help`
for more details
"""
from setuptools import setup, find_packages

# This file is made so that the CI can build a package instead of failing the step.
#  There's no intent on ever publishing this package.

setup(name="autoreduce_actions",
      version="1.0.0",
      description="ISIS Autoreduce common Github actions",
      author="ISIS Autoreduction Team",
      url="https://github.com/autoreduction/autoreduce-actions/",
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
      ])
