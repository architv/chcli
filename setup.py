#!/usr/bin/env python

from setuptools import setup
import sys

setup(
    name='challenge-cli',
    version='0.0.1.0',
    description='Programming challenges for hackers',
    author='Archit Verma',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = "programming challenges competitive topcoder codeforces tool cli",
    author_email='architv07@gmail.com',
    url='https://github.com/architv/chcli',
    packages=['challenges'],
    install_requires=[
        "click>=5.0",
        "requests==2.7.0"
    ] + (["colorama==0.3.3"] if "win" in sys.platform else []),
    entry_points = {
        'console_scripts': [
            'challenges = challenges.cli:main'
      ],
    }
)
