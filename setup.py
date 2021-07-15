from setuptools import setup
from distutils.core import setup
from os import path

setup(
  name = 'internode',
  packages = ['internode'],
  version = '1.1.1',
  license='MIT',
  description = 'Python library to access the Internode API: https://customer-webtools-api.internode.on.net/api/v1.5',
  long_description="""Internode is a package to pull data from https://customer-webtools-api.internode.on.net/api/v1.5. To use the Internode API you need a valid account with Internode.

## Requirements
- Install Python 3.9 (for all users)
- Pip install requests

## Usage

Connect to Internode API:

    import internode
    Internode = internode.api("user.name@outlook.com", "password")

To get service information use the following:

    Internode.getservice()

To get current usage information use the following:

    Internode.getusage()

To get the last day's history information use the following:

    Internode.gethistory()

Full example:

    Internode = internode.api("user.name@outlook.com", "password")
    if (not Internode.Error):
        Internode.getservice()
        print(Internode.service)
        
        Internode.getusage()
        print(Internode.usage)
        
        Internode.gethistory()
        print(Internode.history)
        
    else:
        print(Internode.Error)""",
  long_description_content_type='text/markdown',
  author = 'Leigh Curran',
  author_email = 'InternodePy@outlook.com',
  url = 'https://github.com/leighcurran/AuroraPlus',
  keywords = ['Internode', 'API'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)