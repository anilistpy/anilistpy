import requests
import json

from anilistpy.utils import videoLink

class Anime:
    # init function
    # takes 1 arg -> sQ: id of the anime  
    def __init__(self, sQ):
        self.id = sQ
        #graphql api query
        query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) {
  Page(page: $page, perPage: $perPage) {
    media(id: $id, search: $search, type: ANIME) {
      id
      title {
        romaji
        english
        native
      }
      episodes
      description
      format
      status
      duration
      genres
      tags {
        name
      }
      studios {
        nodes {
          name
        }
      }
      startDate {
        year
        month
        day
      }
      endDate {
        year
        month
        day
      }
      season
      seasonYear
      seasonInt
      countryOfOrigin
      coverImage {
        medium
        large
        extraLarge
      }
      bannerImage
      source
      hashtag
      synonyms
      meanScore
      averageScore
      trailer {
        id
        thumbnail
        site
      }
      staff(sort: FAVOURITES_DESC) {
        edges {
          node {
            name {
              full
            }
            id
          }
        }
      }
      characters(role: MAIN) {
        edges {
          node {
            name {
              full
            }
          }
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
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Page"]["media"]

    # reloads the object. calls the init function again      
    def reload(self):
        self.__init__(self.id)
    # returns the raw json returned from the api request
    def json(self):
        return self.raw
    
    # returns the title
    def title(self, LA: str): # LA options: {romaji}{english}{native}
        return self.media[0]["title"][LA]
    
    # returns the episodes
    def episodes(self):
        return self.media[0]["episodes"]
    
    # returns the anime description in md format
    def description(self):
        return self.media[0]["description"]
    
    # returns the duration of a single episode in minutes
    def duration(self):
        return self.media[0]["duration"]
    
    # returns a list of genres 
    def genres(self):
        return self.media[0]["genres"]
    
    # returns the average score, out of 100
    def averageScore(self):
        return self.media[0]["averageScore"]   
    
    # returns the mean score
    def meanScore(self):
      return self.media[0]["meanScore"]

    # returns a list of tags     
    def tags(self):
      node = self.media[0]["tags"]
      return_list = []
      for i in range(0, len(node)):
        return_list.append(node[i]["name"])
        
      return return_list
    
    # returns the names of studios involved
    def studios(self):
      node = self.media[0]["studios"]["nodes"]
      return_list = []
      for i in range(0, len(node)):
        return_list.append(node[i]["name"])
      
      return return_list
    
    # returns the names/id of staffs involved
    # getID : True returns the list of id  
    # getID : False returns the list of name 
    def staff(self, getID: bool):
      _edges_staff = self.media[0]["staff"]["edges"]
      return_list = []
      
      if getID:
        for i in range(0, len(_edges_staff)):
          return_list.append(_edges_staff[i]["node"]["id"])
        
      elif getID is False:
        for i in range(0,len(_edges_staff)):
          return_list.append(_edges_staff[i]["node"]["name"]["full"])
      else: 
        return "error"
      
      return return_list

    # returns the season it aired on
    def season(self):
        return self.media[0]["season"]
    
    # returns a dict of the starting date
    def startDate(self):
        return self.media[0]["startDate"]
    
    # returns a dict of the ending date
    def endDate(self):
        return self.media[0]["endDate"]
    
    # returns the url of the cover image, large ,medium and extraLarge
    def coverImage(self, SIZE):
        try:
          return self.media[0]["coverImage"][SIZE]
        except KeyError:
          return "key error: arg SIZE is incorrect"
    
    # returns the url of the banner image
    def bannerImage(self):
        return self.media[0]["bannerImage"]
    
    # returns the status of the media
    def status(self):
        return self.media[0]["status"]
    
    # returns offical hashtags
    def hashtag(self):
      return self.media[0]["hashtag"]
    
    # returns synonyms 
    def synonyms(self):
      return self.media[0]["synonyms"]
    
    # returns country of origin
    def countryOfOrigin(self):
      return self.media[0]["countryOfOrigin"]
    
    # returns trailer link
    def trailerlink(self):
      site = self.media[0]["trailer"]["site"]
      id = self.media[0]["trailer"]["id"]
      return videoLink(site, id)
    
    #returns trailer thubmnail
    def trailer_thumbnail(self):
      return self.media[0]["trailer"]["thumbnail"]