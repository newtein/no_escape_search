from firebase import firebase

firebase=firebase.FirebaseApplication('https://newhash-b2715.firebaseio.com')
  


def tofirebase(strn,lnum,fname):
  if(len(strn)>=5):  
    strn=strn.lower()
    num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
    print(num,strn,lnum,fname)
    
    snum='/'+str(num)
  
    result = firebase.post(snum,{'file':fname,'word':strn,'line':lnum})
    
  return;
