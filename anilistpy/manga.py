import requests
import json
class Manga:
    def __init__(self, sQ):
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
        raw = json.loads(response.text)
        print(raw)
        self.media = raw["data"]["Page"]["media"]
           

    def title(self): 
        return self.media[0]["title"]["romaji"]
    def chapters(self):
        return self.media[0]["chapters"]
    def description(self):
        return self.media[0]["description"]
    def genres(self):
        return self.media[0]["genres"]
    def averageScore(self):
        return self.media[0]["averageScore"]    
    def tags(self):
        return self.media[0]["tags"]
    def staffs(self):
        return self.media[0]["staff"]["nodes"][0]["name"]["full"]