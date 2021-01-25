import requests
import json

class MediaList:
    def __init__(self, username, medium, status):
        query = '''
query ($username: String, $type: MediaType, $status: MediaListStatus) {
  MediaListCollection(userName: $username, type: $type, status: $status) {
    lists {
      entries {
        media {
          id
          title {
            english
            romaji
          }
        }
      }
    }
  }
}
        '''
        variables = {
            'username': username,
            'type': medium,
            'status': status
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})
        
        self.raw = json.loads(response.text)["data"]["MediaListCollection"]["lists"][0]["entries"]
        
    def title_list(self, LA):
        _title_list = []
        for i in range(0,len(self.raw)):
            _title_list.append(self.raw[i]["media"]["title"][LA])
        
        return _title_list
    
    def id_list(self):
        _id_list = []
        for i in range(0, len(self.raw)):
            _id_list.append(self.raw[i]["media"]["id"])
        
        return _id_list
    
