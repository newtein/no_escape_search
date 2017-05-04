import csv
import io
import os
import to_firebase as fire
import pdfscan as pdf


def csv_to_text(fname):
    file=open(fname, "r")
    reader = csv.reader(file)
    col=len(next(reader))
    l=0
    for line in reader:
      for i in range (0,col):
         if(len(line[i])>=5):
           fire.tofirebase(line[i],l,fname)
           print(line[i],l,fname)
      l=l+1
    return;

def txt_to_txt(fname):
    fo = open(fname, 'r')

    ctr = 0
    w = fo.readlines()
    for each in w:
     ctr += 1
     strn=each.split()
     for words in strn:
      if(len(words)>5):  
        fire.tofirebase(words,ctr,fname)
    

def start(files):

  no_scan=["t.csv","tb.csv","dump.txt"]
  if files not in no_scan:
    filename, file_ext = os.path.splitext(files)
    print( filename)
    if(file_ext=='.csv'):
        csv_to_text(files)
        return 1
    if(file_ext=='.pdf'):
        pdf.pdf_to_text(files)
        return 1
    if(file_ext=='.txt'):
        txt_to_txt(files)
        return 1
        

