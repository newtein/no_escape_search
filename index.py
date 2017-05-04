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
        self.width=450
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
        
        strn=str(strn)
       
        
        num=(ord(strn[0])*456976+ord(strn[1])*17576+ord(strn[2])*676+ord(strn[3])*26+ord(strn[4])*1)
        print(strn,num)
        data_file=firebase.get(str(num),None)
   
        data = json.loads(json.dumps(data_file))

        x=0
        
        for key, value in data.items():
          print(key)
          self.tableWidget.setItem(x,0, QTableWidgetItem(str(key)))
          
          for key2, val2 in value.items():
             col=2
             for key3,val3 in val2.items():
                print(key3,val3)
               
                
                self.tableWidget.setItem(x,col, QTableWidgetItem(str(val3)))
                col=1
             x=x+1
             

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(9)
        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setHorizontalHeaderLabels(['Word', 'Filename', 'Line/Page(.pdf)'])
        self.tableWidget.move(0,0)           
    
    
         


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
