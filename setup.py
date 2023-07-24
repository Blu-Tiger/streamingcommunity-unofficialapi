from setuptools import setup, find_namespace_packages

setup(
    name="streamingcommunity_unofficialapi",
    author="Beqir Stafa",
    author_email="beqirstafa@gmail.com",
    url="https://github.com/Blu-Tiger/streamingcommunity-unofficialapi",
    description="A simple unofficial api for the italian StreamingCommunity website.",
    version="0.0.3.1",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    install_requires=[
        "setuptools>=61.0",
        "bs4",
        "time",
        "hashlib",
        "base64",
        "json",
        "re",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)