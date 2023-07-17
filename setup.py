from setuptools import find_packages, setup

setup(
    name="my_first_lib",
    version="0.0.1",
    author="Wenfeng Qiu",
    url="https://github.com/wenfengqiu/my_first_lib",
    author_email="wenfengqiu@hotmail.com",
    description="A simple Python library for test purpose",
    packages=["my_first_lib"],  # Add internal libraries required to be installed
    install_requires=[],  # Add any dependencies your library requires
)
