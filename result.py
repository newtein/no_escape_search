import json
from firebase import firebase
from pprint import pprint
firebase=firebase.FirebaseApplication('https://no-escape-search.firebaseio.com/')

data_file=firebase.get("47315202",None)
   
data = json.loads(json.dumps(data_file))


for key, value in data.items():
    print(key)
    for key2, val2 in value.items():
        for key3,val3 in val2.items():
            print(key3,val3)
