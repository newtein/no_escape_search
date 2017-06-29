import os,csv
import buildbase as bbb
def directory():
    #path="abc"
    l=os.listdir()
    c=0
    temp=""
    dir=[]
    while  l:
        try:
           temp=os.listdir(l[0])
           #print(temp)
        except:
            #print("Open File",l[0],c)
            dir.append(l[0])
            c+=1
            del l[0]
        else:    
            for i in range(0,len(temp)):
              if len(temp[i][0])>0:
                 if temp[i][0]!=".":   
                    temp[i]= l[0]+"/"+temp[i]
              else:
                del(temp[i])
           
            #print("ByeBye ",l[0])    
            del(l[0])    
            l.extend(temp)
    return dir
    


def tempcreate():
 filelist=directory()
 print(type(filelist))
 if "dump.txt" not in filelist:
   if "t.csv" in filelist:
     old="t.csv"
     new="tb.csv"
   elif "tb.csv" in filelist:
     old="tb.csv"  
     new="t.csv"
   else:
     ftp=open("t.csv","w")
     ftp.close()
     old="t.csv"
     new="tb.csv"
     
   tempo=open(old,"r")
   tempn=open(new,"w",newline='')
   
   reader=csv.reader(tempo)
   writer=csv.writer(tempn)
   csv_file=[]
   csv_opr=[]
   for lines in reader:
       csv_file.append(lines[0])
       csv_opr.append(lines[1])
   
   avail_ext=[".txt",".csv",".pdf"]
   no_scan=["t.csv","tb.csv","dump.txt"]
   for file in filelist:
     fname,fext=os.path.splitext(file)  
     if fext in avail_ext and file not in no_scan:
         
       if file in csv_file:
           index=csv_file.index(file)
           writer.writerow([file,csv_opr[index]])
       else:
           
           writer.writerow([file,"0"])
   tempo.close()
   tempn.close()
   os.remove(old)
  
   newfile=open(new,"r")
   reader2=csv.reader(newfile)
   dump=open("dump.txt","w")
   fool=0
   for lines in reader2:
       if(int(lines[1])==0):
           fool=1
           tempfile=lines[0].replace(" ","777")
           dump.write(new+" "+tempfile+" 0")
           dump.close()
           offset="0"
           result=bbb.start_init(lines[0],offset)
           print(result,"^^^^")
           if(result==1):
               
               os.remove("dump.txt")
               newfile.close()
               updateone(new,lines[0])
               break
   if(fool==0):
        newfile.close()
        dump.close()
        os.remove("dump.txt")
   else:
        newfile.close()
        tempcreate()
        
           
           
           

 else:
     fptr=open("dump.txt","r")
     w=fptr.readline()
     words=w.split()
     oldf=words[0]
     dumpedf=words[1].replace("777"," ")
     offset=words[-1];
     print(dumpedf,offset)
     fptr.close()
     result=bbb.start_init(dumpedf,offset)
     if(result==1):
            os.remove("dump.txt")
            
            updateone(oldf,dumpedf)
            
            
 return

def updateone(filename,f):
   if filename=="t.csv": 
     old="t.csv"
     new="tb.csv"
   else:
     old="tb.csv"  
     new="t.csv"
   tempo=open(old,"r")
   tempn=open(new,"w",newline='')

   reader=csv.reader(tempo)
   writer=csv.writer(tempn)

   for lines in reader:
       if(lines[0]==f):
           print("------------>written")
           writer.writerow([f,"1"])
       else:
           writer.writerow(lines)
   tempo.close()
   tempn.close()
   os.remove(old)       
   return        



tempcreate()    
     
