import requests
import json

class User:
    def username(accessToken):
        mutation = '''
query ($id: Int) {
  Viewer{
    name
  }
  Media(id: $id){
    id
  }
}    '''
        variables = {
            'id' : 1
        }
        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        url = 'https://graphql.anilist.co'
        response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)

        raw = json.loads(response.text)

        return raw["data"]["Viewer"]["name"]      
    '''
    user mutation api
    def UpdateUser()
    '''
    def updatebio(accessToken, bio):
        mutation = '''
mutation ($bio: String) {
    UpdateUser (about: $bio) {
        about
    }
}
        '''
        variables = {
            'bio' : bio
        }

        headers = {
            'Authorization': 'Bearer ' + accessToken,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        url = 'https://graphql.anilist.co'
        response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)

        raw = json.loads(response.text)

        return raw
