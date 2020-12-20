# Anilistpy ![anilistpy](https://avatars3.githubusercontent.com/u/75199724?s=30&v=4)

[![Build Status](https://travis-ci.com/anilistpy/anilistpy.svg?branch=master)](https://travis-ci.com/anilistpy/anilistpy)
[![CodeFactor](https://www.codefactor.io/repository/github/anilistpy/anilistpy/badge)](https://www.codefactor.io/repository/github/anilistpy/anilistpy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/anilistpy)
[![pypi verison](https://img.shields.io/pypi/v/anilistpy.svg)](https://pypi.org/project/anilistpy/)
[![GitHub license](https://img.shields.io/github/license/anilistpy/anilistpy)](https://github.com/anilistpy/anilistpy/blob/master/license)

An easy to use python3 wrapper for anilist.co APIv2

```
pip install anilistpy
```
 
Documenation and Examples [here](https://anilistpy.readthedocs.io/)

```py
# new in v0.0.3
```py
print(anime.staff(getID=True))   # list of staffs ids
print(anime.staff(getID=False))  # list of staff names

print(anime.trailer_thumbnail()) # image link for trailer's thumbnail
print(anime.trailerlink())       # video link for the trailer
print(anime.synonyms())          # synonyms 
print(anime.hashtag())           # offical hashtags
print(anime.countryOfOrigin())   # country of origin 
```



![agpl3](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/AGPLv3_Logo.svg/200px-AGPLv3_Logo.svg.png)