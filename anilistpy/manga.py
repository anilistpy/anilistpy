import requests
import json
class Manga:
    def __init__(self, sQ):
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
           
    def reload(self):
        self.__init__(self.id)
    def json(self):
        return self.raw
    def title(self, LA): # LA options: {romaji}{english}
        return self.media[0]["title"][LA]
    def chapters(self):
        return self.media[0]["chapters"]
    def volumes(self):
        return self.media[0]["volumes"]
    def description(self):
        return self.media[0]["description"]
    def genres(self):
        return self.media[0]["genres"]
    def averageScore(self):
        return self.media[0]["averageScore"]    
    def tags(self):
        return self.media[0]["tags"]
    def staffs(self):
        node = self.media[0]["staff"]["nodes"]
        slist = []
        for i in range(0, int(len(node))):
            sname = node[i]["name"]["full"] 
            slist.append(sname)
        return slist
    def startDate(self):
        return self.media[0]["startDate"]
    def endDate(self):
        return self.media[0]["endDate"]
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
            
    def bannerImage(self):
        return self.media[0]["bannerImage"]
    

