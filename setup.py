#!usr/bin/env python3
"""
safemd – Safety first markdown rendering

Author: Alexander Hultnér, 2018
"""

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="safemd",
    author="Alexander Hultnér",
    author_email="ahultner@gmail.com",
    maintainer="Alexander Hultnér",
    maintainer_email="ahultner@gmail.com",
    url="https://github.com/Hultner/safemd/",
    description="A markdown renderer focusing on security first",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="18.10.1",
    py_modules=["app"],
    install_requires=["cmarkgfm", "bleach"],
    extras_require={"dev": ["black", "pytest", "twine", "pytest-cov", "codacy-coverage"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
