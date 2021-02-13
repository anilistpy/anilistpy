import requests
import json

class searchStudio:
    def __init__(self, sQ):
        query = '''
query ($sQ: String) {
  Page(page: 1, perPage: 6) {
    studios(search: $sQ) {
      id
      name
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
        self.media = raw["data"]["Page"]["studios"]
    
    def _test(self):
        return True

    def name(self, resultnumber: int):
        return self.media[resultnumber]["name"]
    def id(self, resultnumber: int):
        return self.media[resultnumber]["id"]