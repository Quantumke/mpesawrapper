#setup file from mpesa wrapper

from setuptools import setup

setup(name='mpesawrapper',
      version='0.1',
      description='python wrapper for the new mpesa daraja api',
      url='http://github.com/quatumke/mpesawrapper',
      author='Benson Nguru',
      author_email='nguruben@gmail.com',
      license='MIT',
      packages=['mpesawrapper'],
      install_requires=[
            'nose',
            'requests',
            'uplink',
            'validators',
            'rollbar',
            'sphinx_rtd_theme'
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )