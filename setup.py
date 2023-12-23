"""
Flask-Translator
-------------

Flask-Translator is a quick and easy-to-use extension for Flask projects, enabling translation from YAML files.
"""
from setuptools import setup

setup(
    name='Flask-Translator',
    version='1.0',
    url='https://github.com/inalbilal/flask-translator/',
    license='BSD',
    author='Bilal Inal',
    author_email='01bilalinal@gmail.com',
    description='Flask-Translator is a quick and easy-to-use extension for Flask projects, enabling translation from '
                'YAML files.',
    long_description=__doc__,
    py_modules=['flask_translator'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'PyYAML'
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
