"""Python setup.py for data_driven_ris_deployment package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("data_driven_ris_deployment", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="data_driven_ris_deployment",
    version=read("data_driven_ris_deployment", "VERSION"),
    description="Awesome data_driven_ris_deployment created by Telefonica-Scientific-Research",
    url="https://github.com/Telefonica-Scientific-Research/data_driven_RIS_deployment/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Telefonica-Scientific-Research",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["data_driven_ris_deployment = data_driven_ris_deployment.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
