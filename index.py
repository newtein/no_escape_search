import sys
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton,QLabel,QFileDialog, QWidget,QInputDialog, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import json
from firebase import firebase

firebase=firebase.FirebaseApplication('https://no-escape-search.firebaseio.com/')

class App(QWidget):
    temp_container=[]
    keywords=[]
    def __init__(self):
        super().__init__()
        self.title="No-Escape Search"
        self.left=80
        self.top=50
        self.width=550
        self.height=420
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.textbox=QLineEdit(self)       
        self.textbox.move(20,20)
        self.textbox.resize(280,40)
        self.button=QPushButton('Search',self)
        self.button.move(20,80)
        strn=self.button.clicked.connect(self.on_click)
        print(strn)
        self.createTable()
        self.layout = QVBoxLayout()
        self.next=QPushButton('Next >>',self)
        self.next.clicked.connect(self.show_next)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button) 
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.next)
        
        self.setLayout(self.layout)        
        self.show()


    @pyqtSlot()
    def on_click(self):
         strn=self.textbox.text()
         keywords=strn.split()
         print("???",len(keywords))
         
         for keyword in keywords:
             if(len(strn)<5):

                 QMessageBox.question(self,"Attention","Enter string greater than 5 characters",QMessageBox.Ok)
             else:
                data=self.get_data_from_firebase(keyword)
               
                if (data==None):
                    QMessageBox.question(self,"Attention","No Match Found",QMessageBox.Ok)
                    self.setblank()
                else: 
                    temp=self.json_to_datastructure(data)
                    print(temp)
                    self.temp_container.append(temp)
         if(len(keywords)==1):
             row=self.display_keyword(keywords[0],self.temp_container[0])
             row=self.display_suggestions(keywords[0],self.temp_container[0],row)
         else:
             row=self.find_intersection(keywords,self.temp_container)
         return row

    def show_next(self):
          print("Hey")
            


    def find_intersection(self,keywords,temp_container):
            print("ok")
            sets=[]
            list_iter=0
            for keyword in keywords:
                build_set=set(temp_container[list_iter][keyword])
                sets.append(build_set)
                list_iter+=1
            row=0
            col=0
            files=set.intersection(*sets)
            display_str=" ".join(keywords)
            self.tableWidget.setItem(row,col, QTableWidgetItem(display_str))
            for file in files:
                page=self.intersected(temp_container,file,keywords)
                if page:
                    page=sorted(page)
                    print(page)
                    col+=1
                    self.tableWidget.setItem(row,col, QTableWidgetItem(str(file)))
                    col+=1
                    page_str=self.process_page(file,page)
                    self.tableWidget.setItem(row,col, QTableWidgetItem(str(page_str)))
                    row+=1
                    col=0
            return row

    def intersect(self,a, b):
          return list(set(a) & set(b))
        

    def intersected(self,temp_container,file,keyword):
        sets=[]
        for i in range(0,len(temp_container)):
            build_set=set(temp_container[i][keyword[i]][file])
            sets.append(build_set)
        return set.intersection(*sets)
    
            
    def display_keyword(self,strn,temp):                           
            row=0
            col=0
            if strn in temp:                 
                self.tableWidget.setItem(row,col, QTableWidgetItem(str(strn)))
                for file, page in temp[strn].items():
                    col+=1
                    self.tableWidget.setItem(row,col, QTableWidgetItem(str(file)))
                    col+=1
                    page_str=self.process_page(file,page)
                    self.tableWidget.setItem(row,col, QTableWidgetItem(str(page_str)))
                    row+=1
                    col=0
            return row

        
    def display_suggestions(self,strn,temp,row):
            col=0
            offset=row+9
            for suggestion in temp:
                if suggestion!=strn:
                    self.tableWidget.setItem(row,col, QTableWidgetItem(str(suggestion)))
                    for file, page in temp[suggestion].items():
                        col+=1                                
                        self.tableWidget.setItem(row,col, QTableWidgetItem(str(file)))
                        col+=1
                        page_str=self.process_page(file,page)                             
                        self.tableWidget.setItem(row,col, QTableWidgetItem(str(page_str)))
                        row+=1
                        col=0
                        if(row==offset):
                              break
            return row                

                        
    def get_data_from_firebase(self,strn):
        strn=str(strn).lower()       
        self.setblank()
        num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
        print(strn,num)
        data_file=firebase.get(str(num),None)   
        data = json.loads(json.dumps(data_file))
        return data

        
    def json_to_datastructure(self,data):
          temp={}
          for words, others2 in data.items():                        
                temp[words]={}
                for unique_key, detail in others2.items():
                    pospack, filepack=detail.items()            
                    if(pospack[0]=="file"):
                        pospack,filepack=filepack,pospack
                    if filepack[1] not in temp[words]:
                        temp[words][filepack[1]]=[]
                    temp[words][filepack[1]].append(pospack[1])
                for files in temp[words]:    
                    temp[words][files].sort()
          return temp          

                    
    def setblank(self):
        for i in range(0,9):
            self.tableWidget.setItem(i,0, QTableWidgetItem(""))
            self.tableWidget.setItem(i,1, QTableWidgetItem(""))
            self.tableWidget.setItem(i,2, QTableWidgetItem(""))

        
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(9)        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setHorizontalHeaderLabels(['Suggestions', 'Filename', 'Position'])
        self.tableWidget.move(0,0)           
    
    
    def process_page(self,file,page):
        st=""
        if(file.find("txt",0,len(file))>-1):  
            st="  Line(s): "
        elif(file.find("pdf",0,len(file)))>-1:
            st="  Page(s): "
        elif(file.find("csv",0,len(file))>-1):
            st="  Row(s): "
        st = st[2:]
        st=st+" "+str(page)[1:-1]
        return st


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
    
