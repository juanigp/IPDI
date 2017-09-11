# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(245, 156)
        self.btn_box = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_box.setGeometry(QtCore.QRect(50, 110, 171, 32))
        self.btn_box.setOrientation(QtCore.Qt.Horizontal)
        self.btn_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_box.setObjectName("btn_box")
        self.piecewise_linear_lbl = QtWidgets.QLabel(Dialog)
        self.piecewise_linear_lbl.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.piecewise_linear_lbl.setObjectName("piecewise_linear_lbl")
        self.scalar_lbl = QtWidgets.QLabel(Dialog)
        self.scalar_lbl.setGeometry(QtCore.QRect(150, 20, 101, 16))
        self.scalar_lbl.setObjectName("scalar_lbl")
        self.scalar_edit = QtWidgets.QLineEdit(Dialog)
        self.scalar_edit.setGeometry(QtCore.QRect(150, 45, 61, 20))
        self.scalar_edit.setObjectName("scalar_edit")
        self.ymin_edit = QtWidgets.QLineEdit(Dialog)
        self.ymin_edit.setGeometry(QtCore.QRect(50, 45, 61, 20))
        self.ymin_edit.setObjectName("ymin_edit")
        self.ymax_edit = QtWidgets.QLineEdit(Dialog)
        self.ymax_edit.setGeometry(QtCore.QRect(50, 71, 61, 20))
        self.ymax_edit.setObjectName("ymax_edit")
        self.ymin_lbl = QtWidgets.QLabel(Dialog)
        self.ymin_lbl.setGeometry(QtCore.QRect(10, 45, 31, 16))
        self.ymin_lbl.setObjectName("ymin_lbl")
        self.ymax_lbl = QtWidgets.QLabel(Dialog)
        self.ymax_lbl.setGeometry(QtCore.QRect(10, 71, 41, 16))
        self.ymax_lbl.setObjectName("ymax_lbl")

        self.retranslateUi(Dialog)
        self.btn_box.accepted.connect(Dialog.accept)
        self.btn_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        Dialog.setWindowTitle('Parametros')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.piecewise_linear_lbl.setText(_translate("Dialog", "Filtro lineal a trozos:"))
        self.scalar_lbl.setText(_translate("Dialog", "Filtro escalar:"))
        self.ymin_lbl.setText(_translate("Dialog", "Y min:"))
        self.ymax_lbl.setText(_translate("Dialog", "Y max:"))
        
    def get_values(self):
        return self.ymin_edit.text(), self.ymax_edit.text(), self.scalar_edit.text()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

