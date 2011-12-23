#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from gluon.import_all import base_modules, contributed_modules
import os
import fnmatch

class reglob:
    def __init__(self, directory, pattern="*"):
        self.stack = [directory]
        self.pattern = pattern
        self.files = []
        self.index = 0
    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                self.index = 0
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
            else:
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                if not (file.startswith('.') or file.startswith('#') or file.endswith('~')) \
                        and fnmatch.fnmatch(file, self.pattern):
                    return fullname

setup(app=['web2py.py'],
      data_files=[
        'NEWINSTALL',
        'ABOUT',
        'LICENSE',
        'VERSION',
        ] + \
          [x for x in reglob('applications/examples')] + \
          [x for x in reglob('applications/welcome')] + \
          [x for x in reglob('applications/admin')],
      options={'py2app': {
            'argv_emulation': True,
            'includes': base_modules,
            'packages': contributed_modules,
            }},
      setup_requires=['py2app'])


