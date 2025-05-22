import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from database.inventario_tintometrico_db import inv_tintometrico_db
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import venta_tintometrico_ui
from database.VENTATT_DB import venta_tintometrico_db
from database.VOLL_DB import vol_tintometrico_db

class ventana_venta_tintometrico(QMainWindow):
    def __init__(self):
        super(ventana_venta_tintometrico, self).__init__()
        self.ui = venta_tintometrico_ui.Ui_Form()
        self.ui.setupUi(self)

        self.bd_inv_tintometrico = inv_tintometrico_db()
        self.bd_venta_tintometrico = venta_tintometrico_db()
        self.bd_vol = vol_tintometrico_db()

        self.ui.pushButton.clicked.connect(self.agregar_volumen)
        self.ui.pushButton_2.clicked.connect(self.desagregar_volumen)

        # Crear modelo de datos
        self.model = InvtintometricoTableModel()
            
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)

    def agregar_volumen(self):
        codigo = self.ui.lineEdit.text()
        volumen = self.ui.lineEdit_2.text()
        if codigo != '' and volumen != '':
            r = self.bd_vol.check(codigo)
            re = r[0]
            if re[0] > 0:
                self.bd_inv_tintometrico.restar_vol_inv(codigo, volumen)
                self.bd_vol.sum_vol(volumen, codigo)
            else:
                self.bd_inv_tintometrico.restar_vol_inv(codigo, volumen)
                self.bd_venta_tintometrico.agregar_tablaventa(codigo)
                self.bd_vol.vol_act(volumen, codigo)
            codigo = self.ui.lineEdit.clear()
            volumen = self.ui.lineEdit_2.clear()

    def desagregar_volumen(self):
        codigo = self.ui.lineEdit.text()
        volumen = self.ui.lineEdit_2.text()
        if codigo != '' and volumen != '':
            self.bd_inv_tintometrico.sumar_vol_inv(codigo, volumen)
            self.bd_vol.rest_vol(volumen, codigo)
            codigo = self.ui.lineEdit.clear()
            volumen = self.ui.lineEdit_2.clear()

class InvtintometricoTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(InvtintometricoTableModel, self).__init__(parent)
        
        # Define los nombres de las columnas
        self.columnas = ["Codigo", "Color", "Volumen", "precio"]
        
        # Crear instancia de Database_inventario y obtener datos
        self.datos = inv_tintometrico_db().mostrar_venta() or []  # Evita el error asignando una lista vacía si es False

    def rowCount(self, parent=None):
        return len(self.datos)

    def columnCount(self, parent=None):
        return len(self.columnas)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        
        if role == Qt.DisplayRole:
            # Verifica si los datos están disponibles y si el índice está dentro de rango
            if 0 <= index.row() < len(self.datos) and 0 <= index.column() < len(self.columnas):
                return self.datos[index.row()][index.column()]
        
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            else:
                return section + 1
        return QVariant()