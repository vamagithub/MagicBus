from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in magicbus_erpnext/__init__.py
from magicbus_erpnext import __version__ as version

setup(
	name="magicbus_erpnext",
	version=version,
	description="Magic Bus ERPNext",
	author="Vaama",
	author_email="vama.mv57@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
