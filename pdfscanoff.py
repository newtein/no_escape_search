from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re
import to_firebase as fire
import os,sys


#define = 0(retrival), define = 1(offset)
def pdf_to_text(firebase,pdfname,offset,define):

    # PDFMiner boilerplate
    
    
    dump=open("dump.txt","a")
    

    # Extract text
    fp1 = open(pdfname, 'rb')
    
    i=0
    cnt1=1
    for page in PDFPage.get_pages(fp1):
            if(cnt1>=offset):
                rsrcmgr = PDFResourceManager()
                sio = io.StringIO()
                codec = 'utf-8'
                laparams = LAParams()
                device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                
                interpreter.process_page(page)
                text = sio.getvalue()
                tot=text.split()
                for stri in tot:
                    stri=re.sub('[^A-Za-z0-9]+', '', stri)
                    if(len(stri)>=5):
                       #print (stri,cnt1)
                       dump.write(" "+str(cnt1))
                       try:
                          fire.tofirebase(firebase,stri,cnt1,pdfname)
                       except:
                         print("#######Aborted")
                         dump.close()
                         os.system("python nes.py")
                         sys.exit()
             
                device.close()
                sio.close()
                if(define==0):
                    break
            
            cnt1=cnt1+1
    fp1.close()

     
    

    return


