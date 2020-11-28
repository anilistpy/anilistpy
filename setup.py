import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anilistpy", 
    version="0.0.1.1",
    author="Aaditya Aryal",
    author_email="aryalaadi123@gmail.com",
    description="API wrapper for anilist.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aadityaaryal/anilistpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)