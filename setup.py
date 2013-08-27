from os import path, system

from distutils.core import setup, Command
from distutils.command.install import install
from distutils.extension import Extension
from Cython.Distutils import build_ext

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='PyDOE',
    version='0.1.0',
    author='Mark Stillwell',
    author_email='marklee@fortawesome.org',
    packages=['pydoe'],
    scripts=['bin/create-plan'],
    url='http://pypi.python.org/pypi/PyDOE/',
    license='LICENSE.txt',
    description='Vector Packing Heurisitcs',
    long_description=open('README.md').read(),
    keywords='',
    classifiers=[
      'Development Status :: 1 - Planning',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
      'Topic :: Scientific/Engineering'
    ],
    cmdclass = {'test': PyTest, 'build_ext' : build_ext},
)
