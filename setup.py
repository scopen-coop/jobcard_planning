from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jobcard_planning/__init__.py
from jobcard_planning import __version__ as version

setup(
	name="jobcard_planning",
	version=version,
	description="Add planned date and calendar (updatable) view for Job Card",
	author="Scopen",
	author_email="contact@scopen.fr",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
