# tests

import anilistpy

def test():
    # anime test
    searchA = anilistpy.animeSearch("gochiusa")
    animeObj = anilistpy.Anime(searchA.id(0))
    _jA = animeObj.json()

    # manga test 
    searchM = anilistpy.mangaSearch("chainsawman")
    mangaObj = anilistpy.Manga(searchM.id(0))
    _jA = mangaObj.json()

    return 0

test()