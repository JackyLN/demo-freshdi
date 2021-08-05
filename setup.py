from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in freshdi/__init__.py
from freshdi import __version__ as version

setup(
	name="freshdi",
	version=version,
	description="Testing demo for freshdi git",
	author="lenghia1991@gmail.com",
	author_email="lenghia1991@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
