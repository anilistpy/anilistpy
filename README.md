# Anilistpy
An easy to use wrapper for anilist.co APIv2


```
pip install anilistpy
```

note: this wraper is in very early stage and more features are to come.
 
Documenation on the the [gh-page](https://anilistpy.github.io)

## example 1
```py

import anilistpy            # pip install anilistpy

id = 1                      #id of the anime 

anime = anilistpy.Anime(id)

print(anime.title())        #prints the romaji title of the anime
print(anime.episodes())     #prints the ammount of episodes of the anime
print(anime.description())  #prints the description
print(anime.genres())       #list of genres the anime falls under
print(anime.tags())         #dict of tags this anime has on anilist
print(anime.studios())      #name of studios involved

mid = 30013                 #id of manga

manga = anilistpy.Manga(mid)

print(manga.title())        #prints the romaji title of the manga
print(manga.chapters())     #prints the ammount of chapters in the manga
print(manga.description())  #prints the description
print(manga.genres())       #list of genres the manga falls under
print(manga.tags())         #dict of tags this manga has on anilist
print(manga.staffs())       #name of staffs involved

```

## example 2
```py
import anilistpy

result = anilistpy.animeSearch("cowboy bebop") # search query

print(result.id(0)) # id(x) where id is from the xth result from the search query
print(result.title(0)) # title(x) where title is from the xth result from the search query

result = anilistpy.mangaSearch("chainsaw man") # search query

print(result.id(0)) # id(x) where id is from the xth result from the search query
print(result.title(0)) # title(x) where title is from the xth result from the search query
```