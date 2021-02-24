import requests
import json

class mangaSearch:
    def __init__(self, sQ):
        query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                media (id: $id, search: $search, type: MANGA, sort: POPULARITY_DESC) {
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
            'perPage': 16,
            'MediaType': "MANGA"
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        raw = json.loads(response.text)
        self.media = raw["data"]["Page"]["media"]
    def id(self, resultnumber: int):
        return self.media[resultnumber]["id"]
    def title(self, resultnumber: int):
        return self.media[resultnumber]["title"]["romaji"]

    def result(self):
        return self.media