
import sys
import os
import re

from setuptools import setup, find_packages

#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

sys.path.insert(0, '.')

import svmlib      

VERSION = svmlib.__version__
        
        
#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

print("Package version: ", VERSION)
print("Found following packages:")
PACKAGES = find_packages()

for name in PACKAGES:
    print("\t", name)

REQUIREMENTS = [
    'antlr4'
]

#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

setup(
    name             = 'plang',
    version          = VERSION,
    description      = 'Pattern matching Language',

    packages         = PACKAGES,
    
    install_requires = REQUIREMENTS,

    # Metadata
    author           = 'Diego Billi',
    author_email     = 'diegobilli@gmail.com',
    url              = 'https://github.com/dbilli/plang',
    
    license          = "GPLv2",
)

#------------------------------------------------------------------------------#

