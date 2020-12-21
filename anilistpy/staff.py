import requests
import json

class Staff:
    def __init__(self, sQ):
        self.id = sQ
        query='''
query ($id: Int) {
  Staff(id: $id, sort: FAVOURITES_DESC) {
    id
    name {
      first
      last
      full
      native
    }
    language
    image {
      large
      medium
    }
    description
    isFavourite
    siteUrl
    staffMedia {
      edges {
        node {
          id
          title {
            romaji
            english
            native
          }
        }
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
        self.media = self.raw["data"]["Staff"]

    def _test(self):
        return self.media
        
