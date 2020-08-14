#! /usr/bin/env python
"""A template for scikit-learn compatible packages."""

import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('curvefit', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'curvefit'
DESCRIPTION = 'A sckit-learn wrapper around scipy.optimize.curve_fit'
with codecs.open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

MAINTAINER = 'bsnacks000'

MAINTAINER_EMAIL = ''
URL = 'https://github.com/bsnacks000/curvefit-estimator.git'

LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/bsnacks000/curvefit-estimator.git'

VERSION = __version__
INSTALL_REQUIRES = [
    'numpy', 
    'scipy', 
    'scikit-learn']

CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7', 
               'Programming Language :: Python :: 3.8']

EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)
