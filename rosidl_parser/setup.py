#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
  packages=['rosidl_parser'],
  package_dir= {'rosidl_parser': 'rosidl_parser'},
  )
  
setup(**setup_args)
