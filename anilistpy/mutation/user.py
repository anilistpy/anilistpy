import requests
import json

class User:
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
