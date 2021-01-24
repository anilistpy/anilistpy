from anilistpy import mutation
import json
token = json.load(open('test/secret.json', 'r'))["token"]

# CHANGING STATUS TO WATCHING 
mutation_result = mutation.Media.setstatus(1, token, "CURRENT")
print("set status")
print(mutation_result)

'''
stdout of this code:

0
'''

# CHANGING BIO
print("change bio")

bio = '''
hello there
'''
mutation_result = mutation.User.updatebio(token, bio)
print(mutation_result)

'''
stdout of this code:

0
'''
print("change score")

# CHANGING SCORE
mutation_result = mutation.Media.setscore(1, token, 70)
print(mutation_result)

# CHANGING PROGRESS

mutation_result = mutation.Media.setprogress(1, token, 3)
print(mutation_result)
