import requests
import json

reg='https://cit-home1.herokuapp.com/api/rs_homework_1'
txt = json.dumps({'user': 20,'1':{"movie 2":2.275,"movie 5":3.785,"movie 6":2.851, "movie 8":3.748,"movie 10":2.029,"movie 17":3.636, "movie 21":2.737,"movie 25":3.033}})
head={'content-type': 'application/json'}

p = requests.post(reg, data=txt, headers=head)
print(p)
print(p.json())
