import requests
import json

class Anime:
    # init function
    # takes 1 arg -> sQ: id of the anime  
    def __init__(self, sQ):
        self.id = sQ
        #graphql api query
        query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                media (id: $id, search: $search, type: ANIME) {
                    id
                    title {
                        romaji
                        english
                    }
                    episodes
                    description
                    duration
                    genres
                    averageScore
                    tags{
                        name
                    }
                    studios {
                        nodes{
                            name
                        }
                    }
                    startDate{
                        year
                        month
                        day
                    }
                    endDate{
                        year
                        month
                        day
                    }
                    season
                    coverImage{
                        medium
                        large
                        extraLarge
                    }
                    bannerImage
                }
            }
        }
        '''

        variables = {
            'id': sQ,
            'page': 1,
            'perPage': 1,
            'MediaType': "ANIME"
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Page"]["media"]

    # reloads the object. calls the init function again      
    def reload(self):
        self.__init__(self.id)
    #returns the raw json returned from the api request
    def json(self):
        return self.raw
    #returns the title, 1 arg: LA 
    def title(self, LA: str): # LA options: {romaji}{english}
        return self.media[0]["title"][LA]
    #returns the episodes
    def episodes(self):
        return self.media[0]["episodes"]
    #returns the anime description in md format
    def description(self):
        return self.media[0]["description"]
    #returns the duration of a single episode in minutes
    def duration(self):
        return self.media[0]["duration"]
    #returns a list of genres 
    def genres(self):
        return self.media[0]["genres"]
    #returns the average score, out of 100
    def averageScore(self):
        return self.media[0]["averageScore"]   
    #returns a dict of tags, will change to list later     
    def tags(self):
        return self.media[0]["tags"]
    #returns the names of studios involved
    def studios(self):
        return self.media[0]["studios"]["nodes"]
    #returns the season it aired on
    def season(self):
        return self.media[0]["season"]
    #returns a dict of the starting date
    def startDate(self):
        return self.media[0]["startDate"]
    #returns a dict of the ending date
    def endDate(self):
        return self.media[0]["endDate"]
    #returns the url of the cover image, arg 1 -> L for large M for medium and EL for extraLarge
    def coverImage(self, SIZE):
        try:
            if SIZE == "L":
                return self.media[0]["coverImage"]["large"]
            elif SIZE == "M":
                return self.media[0]["coverImage"]["medium"]
            elif SIZE == "EL":
                return self.media[0]["coverImage"]["extraLarge"]
        except KeyError:
            print("only large medium or extraLarge on SIZE")
    #returns the url of the banner image
    def bannerImage(self):
        return self.media[0]["bannerImage"]

