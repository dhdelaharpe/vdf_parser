from setuptools import setup, find_packages

setup(
    name='vdf_parser',
    version='0.1',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    url='https://github.com/dhdelaharpe/vdf_parser',
    author='ddlh',
    description='Parsing between vdf format and python dict, based on popular JS "vdf-parser"',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming language :: Python :: 3',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent'
    ],

)
