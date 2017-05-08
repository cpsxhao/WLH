# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\A_MyFiles\Grade2_1\支书工作\WebLearningHelper\Login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import core_old

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.username = ''
        self.password = ''
        Dialog.setObjectName("Dialog")
        Dialog.resize(591, 377)
        Dialog.setMouseTracking(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background:rgb(224, 201, 255)")
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 221, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 72, 15))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 170, 72, 15))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 181, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LogIn)
        self.pushButton.setShortcut("enter")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(150, 220, 91, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 220, 91, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 110, 121, 31))
        self.lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 160, 121, 31))
        self.lineEdit_2.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "清华大学网络学堂"))
        self.label.setText(_translate("Dialog", "清华大学网络学堂"))
        self.label_2.setText(_translate("Dialog", "账号"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.checkBox.setText(_translate("Dialog", "记住密码"))
        self.checkBox_2.setText(_translate("Dialog", "自动登录"))

    def LogIn(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "正在登录..."))
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.course = core_old.logIn(self.username, self.password)
        for i in self.course:
            print(i["name"])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
