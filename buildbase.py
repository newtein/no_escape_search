import csv
import io
import os
from firebase import firebase
from urllib.error import HTTPError
from requests.exceptions import ConnectionError
import sys

import to_firebase as fire
import pdfscanoff as pdf

firebase=firebase.FirebaseApplication('https://no-escape-search.firebaseio.com/')

#firebase=firebase.FirebaseApplication('https://hashtable-df2a9.firebaseio.com/')

def csv_to_text(firebase,fname,offset):
    file=open(fname, "r")
    dump=open("dump.txt","a")
    reader = csv.reader(file)
    col=len(next(reader))
    l=0
    for line in reader:
      for i in range (0,col):
         if(len(line[i])>=5 and l>int(offset)):
           dump.write(" "+str(l))
           try:
                fire.tofirebase(firebase,line[i],l,fname)
                print(line[i],l,fname)
           except:
                 print("#######Aborted")
                 dump.close()
                 os.system("python nes.py")
                 sys.exit()
                    
           
      l=l+1
    return;

def txt_to_txt(firebase,fname,offset):
    fo = open(fname, 'r')
    dump=open("dump.txt","a")
    ctr = 0
    w = fo.readlines()
    for each in w:
     ctr += 1
     if(ctr>int(offset)):
         strn=each.split()
         for words in strn:
          if(len(words)>5):
             dump.write(" "+str(ctr))
             try:
                 fire.tofirebase(firebase,words,ctr,fname)
             except:
                 print("#######Aborted")
                 dump.close()
                 os.system("python nes.py")
                 sys.exit()
                 
                 
    

def start_init(files,offset):

  no_scan=["t.csv","tb.csv","dump.txt"]
  if files not in no_scan:
    filename, file_ext = os.path.splitext(files)
    print( filename)
    if(file_ext=='.csv'):
        csv_to_text(firebase,files,offset)
        return 1
    if(file_ext=='.pdf'):
        pdf.pdf_to_text(firebase,files,int(offset),1)
        return 1
    if(file_ext=='.txt'):
        txt_to_txt(firebase,files,offset)
        return 1
        

