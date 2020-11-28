# Anilistpy
A easy to use api wrapper for anilist.co

note: this wraper is in very early stage and more features are to come

## Usage
```py

import anilistpy #pip install anilistpy

id = 1 #id of the anime 

anime = anilistpy.Anime(id)

print(anime.title()) #prints the romaji title of the anime
print(anime.episodes()) #prints the ammount of episodes of the anime
print(anime.genres()) #list of genres the anime falls under
print(anime.tags()) #dict of tags this anime has on anilist
print(anime.studios()) #name of studios involved

```