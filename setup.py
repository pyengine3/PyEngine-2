from setuptools import setup, find_packages

import pyengine2

setup(
    name="PyEngine-2",
    version=pyengine2.__version__,
    packages=find_packages(),
    author="LavaPower",
    author_email="lavapowe84@gmail.com",
    description="A new clean version of PyEngine using PyGame 2",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),

    include_package_data=True,

    url="http://github.com/pyengine-2D/PyEngine-2",

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: pygame",
        "Intended Audience :: Developers",
    ],
    install_requires=['pygame==2.0.0.dev6'],
)
