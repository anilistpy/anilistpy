import requests
import json

class charSearch:
    def __init__(self, sQ):
        query = '''
        query ($sQ: String) {
        Page(page: 1, perPage: 8){
                characters(search: $sQ){
                    name {
                    full
                    native
                    }
                id
            }    
            }

        }
        '''


        variables = {
            'sQ': sQ
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        raw = json.loads(response.text)
        self.media = raw["data"]["Page"]["characters"]
    def result(self):
        return self.media
    def name(self, resultnumber: int):
        return self.media[resultnumber]["name"]["full"]
    def id(self, resultnumber: int):
        return self.media[resultnumber]["id"]
