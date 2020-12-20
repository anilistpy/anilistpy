import requests
import json
class Manga:
    def __init__(self, sQ):
    # init function
    # takes 1 arg -> sQ: id of the anime 
        self.id = sQ
        query = '''
        query ($id: Int, $page: Int, $perPage: Int, $search: String) {
            Page (page: $page, perPage: $perPage) {
                media (id: $id, search: $search, type: MANGA) {
                    id
                    title {
                        romaji
                    }
                    chapters
                    description
                    genres
                    averageScore
                    volumes
                    tags{
                        name
                    }
                    staff{
                        nodes{
                            name{
                                full
                            }
                        }
                    }
                    startDate{
                        year
                        month
                        day
                    }
                    endDate{
                        year
                        month
                        day
                    }
                    coverImage{
                        medium
                        large
                        extraLarge
                    }
                    bannerImage
                }
            }
        }
        '''

        variables = {
            'id': sQ,
            'page': 1,
            'perPage': 1,
            'MediaType': "MANGA"
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        self.raw = json.loads(response.text)
        self.media = self.raw["data"]["Page"]["media"]

    #reloads the object. calls the init function
    def reload(self):
        self.__init__(self.id)
    #returns the raw json from the api request
    def json(self):
        return self.raw
    #returns the title, 1 arg: LA 
    def title(self, LA): # LA options: {romaji}{english}
        return self.media[0]["title"][LA]
    #returns the numbers of chapters, if the manga has not finished returns 0
    def chapters(self):
        return self.media[0]["chapters"]
    #same as above but with volumes
    def volumes(self):
        return self.media[0]["volumes"]
    #returns the manga description in md format
    def description(self):
        return self.media[0]["description"]
    #returns a list of genres 
    def genres(self):
        return self.media[0]["genres"]
    #returns the average score, out of 100
    def averageScore(self):
        return self.media[0]["averageScore"]   
    #returns a dict of tags, will change to list later     
    def tags(self):
        return self.media[0]["tags"]
    #returns the list of staffs involved
    def staffs(self):
        node = self.media[0]["staff"]["nodes"]
        slist = []
        for i in range(0, int(len(node))):
            sname = node[i]["name"]["full"] 
            slist.append(sname)
        return slist
    #returns a dict of the starting date
    def startDate(self):
        return self.media[0]["startDate"]
    #returns a dict of the ending date
    def endDate(self):
        return self.media[0]["endDate"]
    #returns the url of the cover image, arg 1 -> L for large M for medium and EL for extraLarge
    def coverImage(self, SIZE):
        try:
            if SIZE == "L":
                return self.media[0]["coverImage"]["large"]
            elif SIZE == "M":
                return self.media[0]["coverImage"]["medium"]
            elif SIZE == "EL":
                return self.media[0]["coverImage"]["extraLarge"]
        except KeyError:
            print("only large medium or extraLarge on SIZE")
    #returns the url of the banner image  
    def bannerImage(self):
        return self.media[0]["bannerImage"]
    

