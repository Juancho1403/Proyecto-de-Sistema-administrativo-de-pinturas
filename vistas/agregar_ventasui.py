# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar_ventas.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 440, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 280, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 390, 81, 16))
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 270, 231, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(140, 380, 231, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 91, 16))
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 320, 231, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 330, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 280, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 480, 101, 16))
        self.label_11.setObjectName("label_11")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(140, 480, 231, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 530, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(210, 60, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(460, 380, 231, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(460, 270, 231, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(380, 440, 81, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(140, 430, 231, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(460, 430, 231, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(460, 320, 231, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 390, 31, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Usuario id:"))
        self.label_3.setText(_translate("MainWindow", "Cliente:"))
        self.label_5.setText(_translate("MainWindow", "Impuesto Nacional:"))
        self.label_7.setText(_translate("MainWindow", "Forma de Pago: "))
        self.label.setText(_translate("MainWindow", "Agregar Venta"))
        self.label_6.setText(_translate("MainWindow", "Monto Total: "))
        self.label_4.setText(_translate("MainWindow", "Monto base:"))
        self.label_11.setText(_translate("MainWindow", "Porcentaje:"))
        self.pushButton.setText(_translate("MainWindow", "Agregar Venta"))
        self.label_2.setText(_translate("MainWindow", "Fecha:"))
        self.label_10.setText(_translate("MainWindow", "Observaciones:"))
        self.label_8.setText(_translate("MainWindow", "igtf:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
