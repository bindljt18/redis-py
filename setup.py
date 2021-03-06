#!/usr/bin/env python
import os
import sys

from redis import __version__

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)

except ImportError:

    from distutils.core import setup

    def PyTest(x):
        x

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='tds-redis',
    version=__version__,
    description='Python client for Redis key-value store',
    long_description=long_description,
    url='https://github.com/bindljt18/redis-py.git',
    keywords=['Redis', 'key-value store'],
    packages=['redis'],
    extras_require={
        'hiredis': [
            "hiredis>=0.1.3",
        ],
    },
    tests_require=[
        'mock',
        'pytest>=2.5.0',
    ],
    cmdclass={'test': PyTest},
)
