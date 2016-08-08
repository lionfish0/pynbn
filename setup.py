from setuptools import setup

setup(name='pynbn',
      version='1.0.1',
      description='Access to NBN data from python',
      url='https://github.com/lionfish0/pynbn',
      author='Mike Smith',
      author_email='mike@michaeltsmith.org.uk',
      license='MIT',
      packages=['pynbn'],
      keywords='NBN access wrapper',
      install_requires=['requests'],
      zip_safe=False)
