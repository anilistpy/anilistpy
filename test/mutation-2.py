from anilistpy import mutation
import json
token = json.load(open('test/secret.json', 'r'))["token"]

# CHANGING STATUS TO PLANNING 
mutation_result = mutation.Media.SaveMediaListEntry(1, token, "PLANNING")

print(mutation_result)

'''
stdout of this code:

{'data': {'SaveMediaListEntry': {'id': 162834756, 'status': 'PLANNING'}}}
'''