import requests
import json

class Media:
 
    def setstatus(mediaId, accessToken, status):
        mutation = '''
mutation ($mediaId: Int, $status: MediaListStatus) {
    SaveMediaListEntry (mediaId: $mediaId, status: $status) {
        id
    }
}
        '''
        variables = {
            'mediaId' : mediaId,
            'status' : status
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
    
    def setscore(mediaId, accessToken, score):
        mutation = '''
mutation ($mediaId: Int, $scoreRaw: Int) {
    SaveMediaListEntry (mediaId: $mediaId, scoreRaw: $scoreRaw) {
        id
    }
}
        '''
        variables = {
            'mediaId' : mediaId,
            'scoreRaw' : score
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
    
    def setprogress(mediaId, accessToken, progress):
        mutation = '''
mutation ($mediaId: Int, $progress: Int) {
    SaveMediaListEntry (mediaId: $mediaId, progress: $progress) {
        id
    }
}
        '''
        variables = {
            'mediaId' : mediaId,
            'progress' : progress
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
        
