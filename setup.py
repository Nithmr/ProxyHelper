from distutils.core import setup
import codecs

with codecs.open('README.md', encoding='utf-8') as file:
    long_description = file.read()

setup(name='ProxyHelper',
      version='1.0.0',
      author='None',
      author_email='None',
      description='ProxyHelper is a set of utilities that you can install and forget and it will just work! It will automate all your proxy and tor configuration needs on linux.',
      long_description=long_description,
      license='None',
      url='https://github.com/Nithmr/ProxyHelper',
      packages=['ProxyHelper'],
      classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
