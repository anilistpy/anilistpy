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
    _jM = mangaObj.json()

    # character test
    searchC = anilistpy.charSearch("shamiko")
    chObj = anilistpy.Character(searchC.id(0))
    _jC = chObj.json()

    return 0

test()