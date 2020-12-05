import requests
import json
class Anime:
    def __init__(self, sQ):
        self.id = sQ 
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
           
    def reload(self):
        self.__init__(self.id)
    def json(self):
        return self.raw
    def title(self, LA: str): # LA options: {romaji}{english}
        return self.media[0]["title"][LA]
    def episodes(self):
        return self.media[0]["episodes"]
    def description(self):
        return self.media[0]["description"]
    def duration(self):
        return self.media[0]["duration"]
    def genres(self):
        return self.media[0]["genres"]
    def averageScore(self):
        return self.media[0]["averageScore"]    
    def tags(self):
        return self.media[0]["tags"]
    def studios(self):
        return self.media[0]["studios"]["nodes"]
    def season(self):
        return self.media[0]["season"]
    def startDate(self):
        return self.media[0]["startDate"]
    def endDate(self):
        return self.media[0]["endDate"]
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
    def bannerImage(self):
        return self.media[0]["bannerImage"]

