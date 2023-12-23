"""
Flask-Translator
-------------

Flask-Translator is a quick and easy-to-use extension for Flask projects, enabling translation from YAML files.
"""
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Flask-Translator is a quick and easy-to-use extension for Flask projects, enabling translation from YAML files.'

setup(
    name='Flask-Translator',
    version=VERSION,
    url='https://github.com/inalbilal/flask-translator/',
    license='BSD',
    author='Bilal Inal',
    author_email='01bilalinal@gmail.com',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'Flask',
        'PyYAML'
    ],
    keywords=[
        'Flask',
        'Flask extension',
        'translation',
        'i18n',
        'l10n',
        'multilingual',
        'language',
        'internationalization',
        'localization',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
