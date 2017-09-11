# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'img_processing.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from some_functions import RGB_sum,YIQ_sum, RGB_subtraction, YIQ_subtraction, if_darker, if_lighter
from save_file import Ui_Window


import numpy as np
from scipy import misc
from matplotlib.image import imsave
import os



class ImageProcessor:
    def __init__(self, width, height):
        self._img1 = np.zeros([width, height,4])
        self._img2 = np.zeros([width, height,4])
        self._img3 = np.zeros([width, height,4])
        pass
    
    @property
    def img1(self):
        return self._img1
    
    @img1.setter
    def img1(self, value):
        self._img1 = value
    
    @img1.deleter
    def img1(self):
        pass
    
    @property
    def img2(self):
        return self._img2
    
    @img2.setter
    def img2(self, value):
        self._img2 = value
    
    @img2.deleter
    def img2(self):
        pass    
    
    @property
    def img3(self):
        return self._img3
    
    @img3.setter
    def img3(self, value):
        self._img3 = value
    
    @img3.deleter
    def img3(self):
        pass    

    def process(self, operation):
        if operation == 'Suma RGB clampeada':
            self._img3 = RGB_sum(self._img1, self._img2,'clamped')
        elif operation == 'Suma RGB promediada':
            self._img3 = RGB_sum(self._img1, self._img2,'average')
        elif operation == 'Suma YIQ clampeada':
            self._img3 = YIQ_sum(self._img1, self._img2)
        elif operation == 'If darker':
            self._img3 = if_darker(self._img1, self._img2)
        elif operation == 'If lighter':
            self._img3 = if_lighter(self._img1, self._img2)

        elif operation == 'Resta RGB clampeada':
            self._img3 = RGB_subtraction(self._img1, self._img2,'clamped') 
        elif operation == 'Resta RGB promediada':
            self._img3 = RGB_subtraction(self._img1, self._img2,'average')  
        elif operation == 'Resta YIQ clampeada':
            self._img3 = YIQ_subtraction(self._img1, self._img2)  
        return self._img3
        #...
        
      
        


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 532)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1238, 532))
        MainWindow.setMaximumSize(QtCore.QSize(1238, 532))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img1_lbl.setGeometry(QtCore.QRect(10, 10, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1_lbl.sizePolicy().hasHeightForWidth())
        self.img1_lbl.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.img1_lbl.setPalette(palette)
        self.img1_lbl.setAutoFillBackground(True)
        self.img1_lbl.setText("")
        self.img1_lbl.setObjectName("img1_lbl")
        self.img2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img2_lbl.setGeometry(QtCore.QRect(420, 10, 400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.img2_lbl.setPalette(palette)
        self.img2_lbl.setAutoFillBackground(True)
        self.img2_lbl.setText("")
        self.img2_lbl.setObjectName("img2_lbl")
        self.img3_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img3_lbl.setGeometry(QtCore.QRect(830, 10, 400, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.img3_lbl.setPalette(palette)
        self.img3_lbl.setAutoFillBackground(True)
        self.img3_lbl.setText("")
        self.img3_lbl.setObjectName("img3_lbl")
        self.img1_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.img1_edit.setGeometry(QtCore.QRect(12, 430, 401, 20))
        self.img1_edit.setObjectName("image1_edit")
        self.img2_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.img2_edit.setGeometry(QtCore.QRect(420, 430, 401, 20))
        self.img2_edit.setObjectName("img2_edit")
        self.img1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img1_btn.setGeometry(QtCore.QRect(130, 470, 151, 41))
        self.img1_btn.setObjectName("img1_btn")
        self.img2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img2_btn.setGeometry(QtCore.QRect(550, 470, 151, 41))
        self.img2_btn.setObjectName("img2_btn") 
        self.op_cb = QtWidgets.QComboBox(self.centralwidget)
        self.op_cb.setGeometry(QtCore.QRect(956, 430, 121, 22))
        self.op_cb.setObjectName("op_cb")
        self.op_cb.addItem("")
        self.op_cb.addItem("")
        self.op_cb.addItem("")
        self.op_cb.addItem("")
        self.format_cb = QtWidgets.QComboBox(self.centralwidget)
        self.format_cb.setGeometry(QtCore.QRect(1087, 430, 111, 22))
        self.format_cb.setObjectName("format_cb")
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.format_cb.addItem("")
        self.op_label = QtWidgets.QLabel(self.centralwidget)
        self.op_label.setGeometry(QtCore.QRect(840, 430, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.op_label.setFont(font)
        self.op_label.setObjectName("op_label")
        self.process_btn = QtWidgets.QPushButton(self.centralwidget)
        self.process_btn.setGeometry(QtCore.QRect(910, 468, 141, 41))
        self.process_btn.setObjectName("process_btn")        
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(1060, 468, 141, 41))
        self.save_btn.setObjectName("save_btn")
        self.img1_lbl.raise_()
        self.img2_lbl.raise_()
        self.img3_lbl.raise_()
        self.img1_edit.raise_()
        self.img2_edit.raise_()
        self.img1_btn.raise_()
        self.img2_btn.raise_()
        self.op_cb.raise_()
        self.format_cb.raise_()
        self.op_label.raise_()
        self.save_btn.raise_()
        self.process_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    

        ### 
        #   señales de botones
        self.img1_btn.clicked.connect(self.load_img1)
        self.img2_btn.clicked.connect(self.load_img2)      
        self.process_btn.clicked.connect(self.process)       
        self.save_btn.clicked.connect(self.open_save_window)
        
        self.img_processor = ImageProcessor(512,512)
        
        
        
        ### 
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img1_btn.setText(_translate("MainWindow", "Cargar"))
        self.img2_btn.setText(_translate("MainWindow", "Cargar"))
        self.op_cb.setItemText(0, _translate("MainWindow", "Suma"))
        self.op_cb.setItemText(1, _translate("MainWindow", "Resta"))
        self.op_cb.setItemText(2, _translate("MainWindow", "If lighter"))
        self.op_cb.setItemText(3, _translate("MainWindow", "If darker"))
        self.format_cb.setItemText(0, _translate("MainWindow", "RGB clampeado"))
        self.format_cb.setItemText(1, _translate("MainWindow", "RGB promediado"))
        self.format_cb.setItemText(2, _translate("MainWindow", "YIQ clampeado"))
        self.op_label.setText(_translate("MainWindow", "Operación:"))
        self.process_btn.setText(_translate("MainWindow", "Procesar"))
        self.save_btn.setText(_translate("MainWindow", "Guardar"))



############################

    def load_image(self, file, img):   
        path = os.path.dirname(__file__) + '/' + file
        img = misc.imread(path)   
        return img
    
    def save_image(self, file, img):        
        imsave(file, img)        
        return img    
    
    def show_image(self, img, qlbl):
        
        copy = img.copy()
        height, width, channels = copy.shape
               
        temp = np.zeros([height,width])
        temp = copy[:,:,0].copy()
        temp = np.uint8(np.round(temp))
        
        copy[:,:,0] = copy[:,:,2]
        copy[:,:,2] = temp
            
    
        qtimg=QtGui.QImage(copy.data, width, height, QtGui.QImage.Format_RGB32)
        pixmap=QtGui.QPixmap.fromImage(qtimg)    
        pixmap = pixmap.scaled(qlbl.size(), QtCore.Qt.KeepAspectRatio)

        qlbl.setPixmap(pixmap)
        qlbl.show()  
        return img

                    
#funciones de los botones       
    def load_img1(self):
        self.img_processor.img1 = self.load_image(self.img1_edit.text(), self.img_processor.img1)
        self.show_image(self.img_processor.img1, self.img1_lbl)
        
               
        
    def load_img2(self):
        self.img_processor.img2 = self.load_image(self.img2_edit.text(), self.img_processor.img2)
        self.show_image(self.img_processor.img2, self.img2_lbl)                   
    

    def open_save_window(self):
        self.secondary_window = QtWidgets.QMainWindow()
        self.secondary_ui = Ui_Window(self.img_processor.img3)
        self.secondary_ui.setupUi(self.secondary_window)
        self.secondary_window.show()

        
    def process(self):
        if (self.op_cb.currentText() == 'Suma') and (self.format_cb.currentText() == 'RGB clampeado'):
            self.img_processor.img3 = self.img_processor.process('Suma RGB clampeada')
        
        elif (self.op_cb.currentText() == 'Suma') and (self.format_cb.currentText() == 'RGB promediado'):
            self.img_processor.img3 = self.img_processor.process('Suma RGB promediada')   

        elif (self.op_cb.currentText() == 'Suma') and (self.format_cb.currentText() == 'YIQ clampeado'):
            self.img_processor.img3 = self.img_processor.process('Suma YIQ clampeada')   

        elif (self.op_cb.currentText() == 'Resta') and (self.format_cb.currentText() == 'RGB clampeado'):
            self.img_processor.img3 = self.img_processor.process('Resta RGB clampeada')               

        elif (self.op_cb.currentText() == 'Resta') and (self.format_cb.currentText() == 'RGB promediado'):
            self.img_processor.img3 = self.img_processor.process('Resta RGB promediada')   
            
        elif (self.op_cb.currentText() == 'Resta') and (self.format_cb.currentText() == 'YIQ clampeado'):
            self.img_processor.img3 = self.img_processor.process('Resta YIQ clampeada')      
            
        elif (self.op_cb.currentText() == 'If darker'):
            self.img_processor.img3 = self.img_processor.process('If darker')
 
        elif (self.op_cb.currentText() == 'If lighter'):  
            self.img_processor.img3 = self.img_processor.process('If lighter')           
            
        img3 = self.img_processor.img3.copy() 
     
 
        self.show_image(img3, self.img3_lbl)
        
######################################    

        

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    MainWindow.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()




