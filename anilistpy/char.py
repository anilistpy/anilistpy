import requests
import json

class Character:
    def __init__(self, sQ):
        self.id = sQ
        query='''
query ($id: Int) {
  Character(id: $id, sort: FAVOURITES_DESC) {
    id
    name {
      first
      last
      full
      native
    }
    image {
      large
      medium
    }
    description
    isFavourite
    siteUrl
    media {
      edges {
        node{
          title {
            romaji
            english
            native
            userPreferred
          }
          id
        }
      }
    }
    favourites
  }
}
        '''
        variables = {
            'id': sQ
        }  

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Character"]

    def _test(self):
        return self.media
        
