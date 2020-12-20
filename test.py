# tests

import anilistpy

anime = anilistpy.Anime(113970)
print(anime.status())
print(anime.coverImage("extraLarge"))
print(anime.meanScore())
print(anime.title("native"))
#print(anime.json())

print(anime.staff(getID=True))
print(anime.staff(getID=False))

print(anime.trailer_thumbnail())
print(anime.synonyms())
print(anime.hashtag())
print(anime.countryOfOrigin())

