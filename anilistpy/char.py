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

    def reload(self):
      return self.__init__(self.sQ)
    def json(self):
      return self.raw

    def name(self, format):
        return self.media["name"][format]    
    def image(self, SIZE):
        return self.media["image"][SIZE]
    def description(self):
        return self.media["description"]
    def media(self):
        return self.media["media"]["edges"]["node"]
