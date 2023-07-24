import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamingcommunity-unofficialapi",
    version="0.0.3.4",
    author="Beqir Stafa",
    description="A simple unofficial api for the italian StreamingCommunity website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blu-Tiger/streamingcommunity-unofficialapi",
    packages=setuptools.find_packages(),
    install_requires=[],
	license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Topic :: Utilities",
    ],
    python_requires='>= 3.10',
)