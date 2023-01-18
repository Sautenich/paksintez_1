"""Python setup.py for paksintez_1 package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("paksintez_1", "VERSION")
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
    name="paksintez_1",
    version=read("paksintez_1", "VERSION"),
    description="Awesome paksintez_1 created by Sautenich",
    url="https://github.com/Sautenich/paksintez_1/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Sautenich",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["paksintez_1 = paksintez_1.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
