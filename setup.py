'''
Created on Sep 2, 2012

@author: yoyzhou

Edited by Marcin Kolenda at 12th of October 2017.
'''

from distutils.core import setup

setup(
      name='pyTree',
      version='1.0.8',
      description='A list-derived TREE data structure in Python ',
      author='Marcin Kolenda',
      author_email='marcinkolenda419@gmail.com',
      url='https://github.com/cestrand/pyTree',
      packages=['pyTree'],
      package_dir={'pyTree': 'src/pyTree'},
      classifiers=[
          'Development Status :: 4 - Beta ',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License    ',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
           'Topic :: Software Development'
          ]
       )
