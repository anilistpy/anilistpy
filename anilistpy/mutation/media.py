import requests
import json

class Media:
    def SaveMediaListEntry(mediaId, accessToken, status):
        mutation = '''
mutation ($mediaId: Int, $status: MediaListStatus) {
    SaveMediaListEntry (mediaId: $mediaId, status: $status) {
        id
        status
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
