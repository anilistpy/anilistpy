from anilistpy import mutation
import json
token = json.load(open('test/secret.json', 'r'))["token"]

# CHANGING STATUS TO PLANNING 
mutation_result = mutation.Media.setstatus(1, token, "PLANNING")

print(mutation_result)

'''
stdout of this code:

0
'''

bio = '''
test
test


test
test


test
test
'''
mutation_result = mutation.User.updatebio(token, bio)
'''
stdout of this code:

0
'''
