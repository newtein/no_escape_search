from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re
import to_firebase as fire



def pdf_to_text(pdfname):

    fp = open(pdfname, 'rb')
    i=0
    cnt=1
    for page in PDFPage.get_pages(fp):
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
            if(len(stri)>=5):
               print (stri,cnt)
               fire.tofirebase(stri,cnt,pdfname)
        cnt=cnt+1       
        
        
    sio.close()
    device.close()    
    fp.close()


    return 



