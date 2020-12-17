import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anilistpy", 
    version="0.0.2.1",
    author="kalekale",
    author_email="kalekale.anon@gmail.com",
    description="python API wrapper for anilist.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anilistpy/anilistpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
#python3 -m twine upload --repository pypi dist/* 
#python3 setup.py sdist bdist_wheel