from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streamingcommunity_unofficialapi",
    author="Beqir Stafa",
    author_email="beqirstafa@gmail.com",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blu-Tiger/streamingcommunity-unofficialapi",
    description="A simple unofficial api for the italian StreamingCommunity website.",
    version="0.0.3.1",
    packages=find_packages(),
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
        "Topic :: Utilities",
    ],
    python_requires='>= 3.10',
)