# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_file.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.image import imsave
class Ui_Window(object):
    def __init__(self, file):
        self.file = file
    
    def setupUi(self, Window):
        
        self.Window = Window
        self.Window.setObjectName("Window")
        self.Window.resize(299, 88)
        self.Window.setMinimumSize(QtCore.QSize(299, 88))
        self.Window.setMaximumSize(QtCore.QSize(299, 88))
        self.centralwidget = QtWidgets.QWidget(self.Window)
        self.centralwidget.setObjectName("centralwidget")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(200, 39, 75, 23))
        self.save_btn.setObjectName("save_btn")
        self.file_lbl = QtWidgets.QLabel(self.centralwidget)
        self.file_lbl.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.file_lbl.setObjectName("file_lbl")
        self.file_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.file_edit.setGeometry(QtCore.QRect(10, 40, 171, 20))
        self.file_edit.setObjectName("file_edit")
        self.Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        self.Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.Window)
        self.statusbar.setObjectName("statusbar")
        self.Window.setStatusBar(self.statusbar)

        self.retranslateUi(self.Window)
        QtCore.QMetaObject.connectSlotsByName(self.Window)
        ########
        
        self.save_btn.clicked.connect(self.save_and_close)

        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Guardar archivo", "Guardar archivo"))
        self.save_btn.setText(_translate("Guardar archivo", "Listo!"))
        self.file_lbl.setText(_translate("Guardar archivo", "Nombre y extensión del archivo:"))


        #######
    def get_text(self):
        return self.file_edit.text()
    
    def save_and_close(self):
        file_name = self.file_edit.text()
        if file_name != '':
            imsave(file_name, self.file)
        self.Window.close()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

