from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import to_firebase as fire

def pdf_to_text(pdfname):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(pdfname, 'rb')
    i=0
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        i=i+1
        if(i==3):break
        
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()
    
    tot=text.split()
    for stri in tot:
       if(len(stri)>=5):
           fire.tofirebase()

    # Cleanup
    device.close()
    sio.close()

    return text


        
