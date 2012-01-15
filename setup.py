import sys
import os
from setuptools import setup

version = "0.0.1"

long_description = """

Experimental port of pip to use the distutils2 packaging library.

"""

setup(name="pip2",
      version=version,
      description="Experimental port of pip to use distutils2.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
      ],
      keywords='easy_install distutils2 setuptools egg virtualenv',
      author='OSUPython Senior Design Team',
      author_email='osupython@gmail.com',
      url='http://https://github.com/osupython/pip2',
      license='MIT',
      packages=['pip2', 'pip2.commands'],
      entry_points=dict(console_scripts=['pip2=pip2:main']),
      test_suite='nose.collector',
      tests_require=['nose', 'virtualenv>=1.7', 'scripttest>=1.1.1', 'mock'],
      zip_safe=False)
