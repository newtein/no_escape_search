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
         if(len(line[i])>=5)
           fire.tofirebase(line[i],j,f)
           #print(line[i],l,fname)
      l=l+1
    return;      

l=0
filelist=os.listdir()
for files in filelist:
    filename, file_ext = os.path.splitext(files)
    print( filename)
    if(file_ext=='.csv'):
        csv_to_text(files)
    if(file_ext=='.pdf'):
        pdf.pdf_to_text(files)
        

