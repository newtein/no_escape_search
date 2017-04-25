from firebase import firebase
import json

firebase=firebase.FirebaseApplication('https://newhash-b2715.firebaseio.com')
#result = firebase.post('/6178316',{'file1':'f','word':'w','line':'l'})
result = firebase.get('/36058621',None)



for key, value in result.items():
    for key2,value2 in value.items():
        print(key2,value2)


