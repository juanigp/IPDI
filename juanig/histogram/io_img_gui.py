# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'io_img_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import some_functions as sf
from settings_dialog import Ui_Dialog
from save_file import Ui_Window

import numpy as np
from scipy import misc
from matplotlib.image import imsave
import os


class ImageProcessor:
    def __init__(self, width, height):
        self._img1 = np.zeros([width, height,4])
        self._img2 = np.zeros([width, height,4])
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


    def process(self, fltr, a, b):

        if fltr == 'Raiz cuadrada':
            self._img2 = sf.sqrt_filter(self._img1).copy()
        elif fltr == 'Cuadrado':
            self._img2 = sf.sqr_filter(self._img1).copy()
        elif fltr == 'Escalar':
            self.img2 = sf.scalar_filter(self._img1, a ).copy()
        elif fltr == 'Linear a trozos':
            self.img2 = sf.piecewise_linear_filter(self._img1, a, b ).copy()

        return self.img2
        #...


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 487)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(830, 473))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
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
        self.img_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.img_edit.setGeometry(QtCore.QRect(12, 430, 331, 20))
        self.img_edit.setObjectName("img_edit")
        self.img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_btn.setGeometry(QtCore.QRect(350, 430, 61, 21))
        self.img_btn.setObjectName("img_btn")
        self.filter_lbl = QtWidgets.QLabel(self.centralwidget)
        self.filter_lbl.setGeometry(QtCore.QRect(490, 428, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.filter_lbl.setFont(font)
        self.filter_lbl.setObjectName("filter_lbl")
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(665, 425, 71, 31))
        self.filter_btn.setObjectName("filter_btn")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(748, 425, 71, 31))
        self.save_btn.setObjectName("save_btn")

        self.filter_cb = QtWidgets.QComboBox(self.centralwidget)
        self.filter_cb.setGeometry(QtCore.QRect(540, 429, 111, 22))
        self.filter_cb.setObjectName("filter_cb")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ######

        self.img_processor = ImageProcessor(512,512)

        self.img_btn.clicked.connect(self.load_img)
        self.filter_btn.clicked.connect(self.do_filter)
        self.save_btn.clicked.connect(self.open_save_window)

        width = MainWindow.frameGeometry().width()
        height = MainWindow.frameGeometry().height()

        MainWindow.setMinimumWidth(width)
        MainWindow.setMinimumHeight(height)

        MainWindow.setMaximumWidth(width)
        MainWindow.setMaximumHeight(height)

        MainWindow.setWindowTitle('Operaciones de luminancia')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_btn.setText(_translate("MainWindow", "Cargar"))
        self.filter_lbl.setText(_translate("MainWindow", "Filtro"))
        self.filter_btn.setText(_translate("MainWindow", "Procesar"))
        self.save_btn.setText(_translate("MainWindow", "Guardar"))
        self.filter_cb.setItemText(0, _translate("MainWindow", "Raiz cuadrada"))
        self.filter_cb.setItemText(1, _translate("MainWindow", "Cuadrado"))
        self.filter_cb.setItemText(2, _translate("MainWindow", "Escalar"))
        self.filter_cb.setItemText(3, _translate("MainWindow", "Linear a trozos"))

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




############

    def load_img(self):
        self.img_processor.img1 = self.load_image(self.img_edit.text(), self.img_processor.img1)
        self.show_image(self.img_processor.img1, self.img1_lbl)

    def do_filter(self):
        if (self.filter_cb.currentText() == 'Escalar' ) or (self.filter_cb.currentText() == 'Linear a trozos' ) :
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                Dialog.exec_()
                ymin, ymax, scl = ui.get_values()

                if (ymin == '') and (ymax == ''):
                    self.img_processor.img2 = self.img_processor.process(self.filter_cb.currentText(),float(scl),0)
                else:
                    self.img_processor.img2 = self.img_processor.process(self.filter_cb.currentText(),float(ymin),float(ymax))
        else:
            self.img_processor.img2 = self.img_processor.process(self.filter_cb.currentText(), 0, 0)


        img2 = self.img_processor.img2.copy()
        self.show_image(img2, self.img2_lbl)


    def open_save_window(self):
        self.secondary_window = QtWidgets.QMainWindow()
        self.secondary_ui = Ui_Window(self.img_processor.img2)
        self.secondary_ui.setupUi(self.secondary_window)
        self.secondary_window.show()


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
