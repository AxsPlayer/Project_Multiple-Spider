#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
from __future__ import print_function
from datetime import date
import os
from setuptools import find_packages
from setuptools import setup

# Define project dependent variable.
# -----------------------------------------
NAME = "x-spider"  # Your package name
GITHUB_USERNAME = "AxsPlayer"  # Your GitHub user name
VERSION = __import__(NAME).__version__  # Version of package.
AUTHOR = "AxsPlayer"
AUTHOR_EMAIL = "axsplyer@126.com"
MAINTAINER = "AxsPlayer"
MAINTAINER_EMAIL = "axsplyer@126.com"
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
PACKAGES = [NAME] + ["%s.%s" % (NAME, i) for i in find_packages(NAME)]  # Include all sub packages in package directory.
INCLUDE_PACKAGE_DATA = True  # Include everything in package directory.
PACKAGE_DATA = {"": ["*.*"], }
repository_name = os.path.basename(os.getcwd())  # The project directory name is the GitHub repository name.
URL = "https://github.com/{0}/{1}".format(GITHUB_USERNAME, repository_name)  # Project Url
github_release_tag = str(date.today())  # Use todays date as GitHub release tag
DOWNLOAD_URL = "https://github.com/{0}/{1}/tarball/{2}".format(
    GITHUB_USERNAME, repository_name, github_release_tag)  # Source code download url
CLASSIFIERS = ['License :: OSI Approved :: Apache Software License',
               'Programming Language :: Python :: 2.7']
PYTHON_REQUIRES = '>=2.6, !=3.*'
# PLATFORMS = ["Windows", "MacOS", "Unix"]

# Automatically generate setup parameters
# Short description.
try:
    SHORT_DESCRIPTION = __import__(NAME).__short_description__  # GitHub Short Description
except:
    print("'__short_description__' not found in '%s.__init__.py'!" % NAME)
    SHORT_DESCRIPTION = "No short description!"
# Long description.
try:
    LONG_DESCRIPTION = open("README.md", "rb").read().decode("utf-8")  # README.rst???
except:
    LONG_DESCRIPTION = "No long description!"
# License.
try:
    LICENSE = __import__(NAME).__license__
except:
    print("'__license__' not found in '%s.__init__.py'!" % NAME)
    LICENSE = ""
# Requirement.
try:
    f = open("requirements.txt", "rb")
    REQUIRES = [i.strip() for i in f.read().decode("utf-8").split("\n")]
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

# Setup all the settings.
# -----------------------
setup(
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    packages=PACKAGES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    package_data=PACKAGE_DATA,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    # platforms=PLATFORMS,
    license=LICENSE,
    install_requires=REQUIRES,
    python_requires=PYTHON_REQUIRES,
)

"""
Appendix
--------
::
Frequent used classifiers List = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Development Status :: 6 - Mature",
    "Development Status :: 7 - Inactive",
    "Intended Audience :: Customer Service",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Healthcare Industry",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Legal Industry",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Religion",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",
    "License :: OSI Approved :: BSD License",
    "License :: OSI Approved :: MIT License",
    "License :: OSI Approved :: Apache Software License",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Natural Language :: English",
    "Natural Language :: Chinese (Simplified)",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",

    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3 :: Only",
]


CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

"""