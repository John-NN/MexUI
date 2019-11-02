#!/usr/bin/env python3
from __future__ import absolute_import
from __future__ import print_function
import sys
import os

directory = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(str(directory))
import main

main.Run(sys.argv)

