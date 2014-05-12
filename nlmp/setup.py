from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-nlmp',
    version=version,
    description="This is an extension of the National Live Methane Database project",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Qifeng Bai',
    author_email='bai187@csiro.au',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.nlmp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        extension_nlmp=ckanext.nlmp.plugin:ExampleIDatasetFormPlugin
        project_nlmp=ckanext.nlmp.plugin:NlmpProjectFormPlugin
    ''',
)
