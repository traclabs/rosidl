#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
  packages=['rosidl_adapter'],
  package_dir= {'rosidl_adapter': 'rosidl_adapter'},
  )
  
setup(**setup_args)
