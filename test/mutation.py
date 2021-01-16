import requests
import json

accessToken = json.load(open('test/secret.json', "r"))
mutation = '''
mutation ($mediaId: Int, $status: MediaListStatus) {
    SaveMediaListEntry (mediaId: $mediaId, status: $status) {
        id
        status
    }
}
'''


variables = {
    'mediaId' : 1,
    'status' : "COMPLETED"
}

headers = {
    'Authorization': 'Bearer ' + accessToken["token"],
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
url = 'https://graphql.anilist.co'

response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)
raw = json.loads(response.text)
print(raw)