import os
import sys

from setuptools import setup


# If you change the version here, be sure to also change it in docs/conf.py and
# pip2/__init__.py
version = '0.0.1.dev1'

install_requires = []

if sys.version_info < (3, 3):
    # Distutils2 on PyPI doesn't work for Python 3, so we aren't listing it as
    # a dependency yet (see Github issue 45)
    #install_requires.append('distutils2')
    pass


setup(name="pip2",
      version=version,
      description="Experimental port of pip to use distutils2.",
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
      ],
      keywords='pip packaging distutils2 easy_install setuptools',
      author='OSUPython Senior Design Team',
      author_email='osupython@gmail.com',
      url='http://github.com/osupython/pip2',
      license='MIT',
      packages=['pip2', 'pip2.commands'],
      entry_points=dict(console_scripts=['pip2=pip2:main']),
      install_requires=install_requires,
      zip_safe=False)
