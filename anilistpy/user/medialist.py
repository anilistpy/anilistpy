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
        self.raw = json.loads(response.text)
    
    def raw(self):
        return self.raw
