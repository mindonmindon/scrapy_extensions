# _*_ coding: utf-8 _*_
from setuptools import setup, find_packages

install_requires = [
    'scrapy>=2.0.0',
]

# use "python setup.py bdist_wheel" to pack
# use "python setup.py sdist bdist_wheel upload -r nexus" to pack and upload

setup(
    name='scrapy_extensions',
    version="0.0.1",
    description='scrapy extensions',
    url='',
    author='mindinmindon',
    keywords='scrapy',
    packages=find_packages(exclude=('test',)),
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.8'
)
