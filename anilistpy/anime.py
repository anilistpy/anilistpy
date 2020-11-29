import requests
import json
class Anime:
    def __init__(self, sQ):
        query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                media (id: $id, search: $search, type: ANIME) {
                    id
                    title {
                        romaji
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
        raw = json.loads(response.text)
        self.media = raw["data"]["Page"]["media"]
           

    def title(self): 
        return self.media[0]["title"]["romaji"]
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

class animeSearch:
    def __init__(self, sQ):
        query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                media (id: $id, search: $search, type: ANIME, sort: POPULARITY_DESC) {
                    id
                    title {
                        romaji
                    }
                }
            }
        }
        '''


        variables = {
            'search': sQ,
            'page': 1,
            'perPage': 5,
            'MediaType': "ANIME"
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        raw = json.loads(response.text)
        self.media = raw["data"]["Page"]["media"]
    def id(self, resultnumber: int):
        return self.media[resultnumber]["id"]
    def title(self, resultnumber: int):
        return self.media[resultnumber]["title"]["romaji"]