import ast
import re
import os

from setuptools import setup, find_packages

PACKAGE_NAME = 'python_boilerplate'

here = os.path.abspath(os.path.dirname(__file__))

#with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
#    match = re.search(r'__version__\s+=\s+(.*)', f.read())
#version = str(ast.literal_eval(match.group(1)))

def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                            version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    # metadata
    name=PACKAGE_NAME,
    version=find_version(PACKAGE_NAME, "__version__.py"),

    # options
#    packages=[PACKAGE_NAME],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.4',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
#    entry_points={'console_scripts': ['python-boilerplate=python_boilerplate.cli:main']},
)
