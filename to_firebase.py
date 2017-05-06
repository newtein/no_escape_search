from firebase import firebase
import re

#firebase=firebase.FirebaseApplication('https://no-escape-search.firebaseio.com/')



def tofirebase(firebase,strn,lnum,fname):
  
  strn=re.sub('[^A-Za-z0-9]+', '', strn)
  if(len(strn)>=5):
    strn=strn.lower()
    num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
    print("Hash Index: ",num,"\tWord: ",strn,"\tLine/Page/Row: ",lnum,"Fname: ",fname)
    
    snum=str(num)+'/'+strn
  
    result = firebase.post(snum,{'file':fname,'line':lnum})
    
  return;
