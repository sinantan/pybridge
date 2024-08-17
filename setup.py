from setuptools import setup, find_packages

setup(
    name="pybridge",
    version="0.1.0",
    description="A lightweight library that auto-generates API clients from OpenAPI schemas.",
    author="sinan tan",
    author_email="sinantanwork@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)