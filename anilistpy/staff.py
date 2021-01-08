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
        self.sQ = sQ
        response = requests.post(url, json={'query': query, 'variables': variables})
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Staff"]

    def _test(self):
        return self.media
    
    def reload(self):
      return self.__init__(self.sQ)
    def json(self):
      return self.raw
    
    # return the name of the staff
    def name(self, OPT: str):
      # OPT {full}{first}{last}{native}
      return self.media["name"][OPT]
    
    # returns the language of the staff
    def language(self):
      return self.media["language"]

    # returns the image of the staff
    def image(self, SIZE: str):
      # SIZE {large}{medium}
      return self.media["image"][SIZE]

    # return the description of the staff
    def description(self):
      return self.media["description"]
    
    def staffMedia(self):
      return self.media["staffMedia"]["edges"]
    
    
