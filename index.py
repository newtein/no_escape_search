import sys
from PyQt5.QtWidgets import QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton,QLabel,QFileDialog, QWidget,QInputDialog, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import json
from firebase import firebase

firebase=firebase.FirebaseApplication('https://no-escape-search.firebaseio.com/')

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="No-Escape Search"
        self.left=80
        self.top=50
        self.width=550
        self.height=400
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

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button) 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        
        self.show()

    @pyqtSlot()
    def on_click(self):
         strn=self.textbox.text()
         if(len(strn)<5):
             QMessageBox.question(self,"Attention","Enter string greater than 5 characters",QMessageBox.Ok)
         else:    
            self.displayit(strn)
    def displayit(self,strn):
        
        strn=str(strn).lower()
       
        self.setblank()
        num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
        print(strn,num)
        data_file=firebase.get(str(num),None)
   
        data = json.loads(json.dumps(data_file))
        if (data==None):
            QMessageBox.question(self,"Attention","No Match Found",QMessageBox.Ok)
            self.setblank()
        else: 
                    x=0
                    temp = {}
                    for key, value in data.items():
                      print(key,"|")
                      temp[key] = {}
                      #self.tableWidget.setItem(x,0, QTableWidgetItem(str(key)))
                      
                      for key2, val2 in value.items():
                        col=2
                        filename = ""
                        key3,val3=val2.items()
                        print(key3)
                        if(key3[0]=="file"):
                           if key3[1] not in temp[key]:
                               temp[key][key3[1]]=[]
                              
                           temp[key][key3[1]].append(val3[1])
                        else:
                            if val3[1] not in temp[key]:
                                  temp[key][val3[1]]=[]
                                  
                            temp[key][val3[1]].append(key3[1])
                        
                         
                            
                    x -= 1
                    
                    print (temp)
                    for i in temp:
                        print(i)
                        x += 1
                        col = 0
                        self.tableWidget.setItem(x,col, QTableWidgetItem(str(i)))
                        x -= 1
                        for j in temp[i]:
                            x += 1
                            col = 1
                            print(j, x, col)
                            self.tableWidget.setItem(x,col, QTableWidgetItem(str(j)))
                            col = 2
                            if(j.find("txt",0,len(j))>-1):  
                                st="  Line(s): "
                            elif(j.find("pdf",0,len(j)))>-1:
                                st="  Page(s): "
                            elif(j.find("csv",0,len(j))>-1):
                                st="  Row(s): "
                            for each in temp[i][j]:
                                    st = st  + str(each) +", "
                            st = st[2:]
                            self.tableWidget.setItem(x,col, QTableWidgetItem(st[:-2]))
                           
                
    
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
    
    
         


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
