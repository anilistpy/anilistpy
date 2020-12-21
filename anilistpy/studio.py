import requests
import json

class Studio:
    def __init__(self, sQ):
        self.id = sQ
        query='''
query ($id: Int) {
  Studio(id: $id) {
    id
    name
    media{
      nodes{
        title{
          romaji
        }
        id
        
      }
    }
  }
}

        '''
        variables = {
            'id': sQ
        }  

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Studio"]

    def _test(self):
        return self.media
        
