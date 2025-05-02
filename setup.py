#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2009-2014 MIT ODL Engineering
#
# This file is part of PyLTI.
#

"""
This file provides backward compatibility for tools that don't yet
support pyproject.toml. It simply defers to setuptools.build_meta.
"""

import sys
from setuptools import setup

if __name__ == "__main__":
    # This setup.py is not meant to be run directly
    # It's just a shim for older tools
    print(
        "This setup.py is a shim for tools that don't support pyproject.toml.\n"
        "Please use 'pip install .' or another standards-compliant tool."
    )
    
    # Print Python version compatibility notice if needed
    if sys.version_info < (3, 7):
        print(
            "WARNING: pylti requires Python 3.7+ for full compatibility.\n"
            "You're using Python %s.%s.%s" % sys.version_info[:3]
        )
    
    # Pass arguments to setuptools
    setup()