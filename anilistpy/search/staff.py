import requests
import json

class searchStaff:
    def __init__(self, sQ):
        query = '''
query ($sQ: String) {
  Page(page: 1, perPage: 6) {
    staff(search: $sQ) {
      id
      name {
        first
        last
        full
        native
      }
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
        self.media = raw["data"]["Page"]["staff"]

    def _test(self):
        return True

    def name(self, resultnumber: int):
        return self.media[resultnumber]["name"]["full"]
    def id(self, resultnumber: int):
        return self.media[resultnumber]["id"]