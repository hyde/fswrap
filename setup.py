from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name='fswrap',
    version='0.1.1',
    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/lakshmivyas/fswrap',
    description='An opinionated wrapper on file system and path functions',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    py_modules=['fswrap'],
    tests_require=(
        'nose',
      ),
    test_suite='nose.collector',
)