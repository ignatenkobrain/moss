#! /usr/bin/env python
#
# Copyright (C) 2012-2017 Michael Waskom <mwaskom@nyu.edu>
descr = """Moss: statistical utilities for cognitive neuroscience."""

import os


DISTNAME = 'moss'
DESCRIPTION = descr
MAINTAINER = 'Michael Waskom'
MAINTAINER_EMAIL = 'mwaskom@nyu.edu'
LICENSE = 'BSD (3-clause)'
URL = 'https://github.com/mwaskom/moss'
DOWNLOAD_URL = 'https://github.com/mwaskom/moss'
VERSION = '0.6.dev'

from setuptools import setup

if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        version=VERSION,
        URL=URL,
        download_url=DOWNLOAD_URL,
        packages=['moss', 'moss.tests', 'moss.psychophys', 'moss.external'],
        install_requires=["matplotlib", "numpy", "nibabel", "pandas",
                          "scikit-learn", "scipy", "seaborn", "six"],
        tests_require=["nose", "pytest"],
        scripts=["bin/" + s for s in ["check_mni_reg", "recon_movie",
                                      "recon_status", "recon_qc",
                                      "recon_process_stats", "warp_qc",
                                      "ts_movie"]],
        classifiers=['Intended Audience :: Science/Research',
                     'Programming Language :: Python',
                     'License :: OSI Approved',
                     'Topic :: Scientific/Engineering',           
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
    )
