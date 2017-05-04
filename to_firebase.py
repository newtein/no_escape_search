from firebase import firebase
import re

firebase=firebase.FirebaseApplication('https://hashtable-df2a9.firebaseio.com/')
  


def tofirebase(strn,lnum,fname):
  
  strn=re.sub('[^A-Za-z0-9]+', '', strn)
  if(len(strn)>=5):
    strn=strn.lower()
    num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
    print(num,strn,lnum,fname)
    
    snum=str(num)+'/'+strn
  
    result = firebase.post(snum,{'file':fname,'line':lnum})
    
  return;
