# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
from scipy import misc, fftpack
from some_functions import YIQ, modulo_fase
import os

class ImageProcessor:
    def __init__(self, width, height):
        self._img = np.zeros([width, height,4])
        self._result = np.zeros([width, height,4])
        pass
    
    def initSize(self, width, height):
        self._img = np.zeros([width, height,4])
        self._result = np.zeros([width, height,4])
        pass
    
    @property
    def img(self):
        return self._img
    
    @img.setter
    def img(self, value):
        self._img = value
    
    @img.deleter
    def img(self):
        pass
        
    @property
    def result(self):
        return self._result
    
    @result.setter
    def result(self, value):
        self._result = value
    
    @result.deleter
    def result(self):
        pass    

    def process(self):
        img_YIQ = YIQ(self._img/255)                                   #imagen en YIQ
        Y_array =  np.uint8( np.round( img_YIQ[:,:,0].copy() * 255 ))  #arreglo bidimensional de luminancias

        width, height = Y_array.shape

        dft_array = np.zeros([width,height]) #arreglo de complejos
        mag_array = dft_array.copy()         #arreglo de modulos
        ang_array = dft_array.copy()         #arreglo de fase

        dft_array = np.complex_(dft_array)   #casteo
 
        #transformada por biblioteca
        dft_array = fftpack.fft2(Y_array)    
        mag_array, ang_array = modulo_fase(dft_array)  #modulo y fase
        
        #logartimo
        mag_array[:,:] = np.log10(mag_array[:,:]+1)   # +1 ya que log(0) = 0

        #hallo minimo y maximo
        min_ = mag_array[0,0]
        max_ = mag_array[0,0]
        for i in range(width):
            for j in range(height):
                if mag_array[i,j] > max_:
                    max_ = mag_array[i,j]
                if mag_array[i,j]<min_:
                    min_ = mag_array[i,j]
            
        #interpolacion lineal
        mag_array[:,:] = mag_array[:,:] * 255/(max_ - min_) - min_ * 255/(max_ - min_)


        #traslacion        
        for i in range(width):
            for j in range(height//2):
                aux = mag_array[(i+width//2)%width, (j+height//2)%height ]
                mag_array[(i+width//2)%width, (j+height//2)%height ] = mag_array[i, j]
                mag_array[i,j] = aux



#imagen en escala de grises
        img_dft = np.zeros([width,height,4])
        img_dft[:,:,0] = mag_array.copy()
        img_dft[:,:,1] = mag_array.copy()
        img_dft[:,:,2] = mag_array.copy() 
        img_dft[:,:,3] = 255
        img_dft = np.uint8( np.round( img_dft ) )

        self._result = img_dft
        return self._result
        #...
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 477)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1, 1))
        MainWindow.setMaximumSize(QtCore.QSize(1238, 532))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img_lbl.setGeometry(QtCore.QRect(10, 10, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_lbl.sizePolicy().hasHeightForWidth())
        self.img_lbl.setSizePolicy(sizePolicy)
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
        self.img_lbl.setPalette(palette)
        self.img_lbl.setAutoFillBackground(True)
        self.img_lbl.setText("")
        self.img_lbl.setObjectName("img_lbl")
        self.result_lbl = QtWidgets.QLabel(self.centralwidget)
        self.result_lbl.setGeometry(QtCore.QRect(420, 10, 400, 400))
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
        self.result_lbl.setPalette(palette)
        self.result_lbl.setAutoFillBackground(True)
        self.result_lbl.setText("")
        self.result_lbl.setObjectName("result_lbl")
        self.img_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.img_edit.setGeometry(QtCore.QRect(12, 430, 271, 20))
        self.img_edit.setObjectName("img_edit")
        self.img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_btn.setGeometry(QtCore.QRect(312, 429, 91, 21))
        self.img_btn.setObjectName("img_btn")
        self.transform_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transform_btn.setGeometry(QtCore.QRect(460, 425, 151, 31))
        self.transform_btn.setObjectName("transform_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(630, 425, 141, 31))
        self.save_btn.setObjectName("save_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        ########################################################
        self.img_processor = None
        #   señales de botones
        self.img_btn.clicked.connect(self.load_img)
        self.transform_btn.clicked.connect(self.transform_img)      
        self.save_btn.clicked.connect(self.open_save_window)
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fourier"))
        self.img_btn.setText(_translate("MainWindow", "Cargar"))
        self.transform_btn.setText(_translate("MainWindow", "Transformar!"))
        self.save_btn.setText(_translate("MainWindow", "Guardar"))


############   funciones utiles ############
   
    #cargar una imagen llamada file en una variable llamada img    
    def load_image(self, file, img):   
        path = os.path.dirname(__file__) + '/' + file
        img = misc.imread(path)   
        return img
    
    #guardar una imagen img como un archivo file (no uso este metodo)
    def save_image(self, file, img):        
        misc.imsave(file, img)        
        return img    
    
    #mostrar una imagen img en una QLabel qlbl
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

                    
################ funciones de los botones ####################    

    #cargar imagen a transformar
    def load_img(self):
        img = None
        img = self.load_image(self.img_edit.text(), img)
        width, height, channels = img.shape
        self.img_processor = ImageProcessor(width,height)  #aca se inicializa el objeto ImageProcessor
        self.img_processor.img = img
        self.show_image(self.img_processor.img, self.img_lbl)

    #transformar imagen
    def transform_img(self):
        self.img_processor.result = self.img_processor.process()
        img = self.img_processor.result.copy()
        self.show_image(img, self.result_lbl)

    #guardar imagen
    def open_save_window(self):
        dlg, nosequeeslootroquedevuelve = QtWidgets.QFileDialog().getSaveFileName()
        misc.imsave(dlg,self.img_processor.result)


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

