import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from database.inventario_tintometrico_db import inv_tintometrico_db
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import inventario_tintometrico_ui

class ventana_inv_tintometrico(QMainWindow):
    def __init__(self):
        super(ventana_inv_tintometrico, self).__init__()
        self.ui = inventario_tintometrico_ui.Ui_Form()
        self.ui.setupUi(self)

        self.base_datos = inv_tintometrico_db()

        self.ui.boton_agregar.clicked.connect(self.agregar_tinta)
        self.ui.boton_editar.clicked.connect(self.editar_tinta)
        self.ui.boton_eliminar.clicked.connect(self.eliminar_tinta)

        # Crear modelo de datos
        self.model = InvtintometricoTableModel()
            
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)

    def agregar_tinta(self):
        codigo = self.ui.lineEdit_codigo.text()
        color = self.ui.lineEdit_color.text()
        volumen = self.ui.lineEdit_volumen.text()
        precio = self.ui.lineEdit_precio.text()
        if codigo != '' and color != '' and volumen != '':
            self.base_datos.agregar_inv(codigo, color, volumen, precio)
            self.ui.lineEdit_codigo.clear()
            self.ui.lineEdit_color.clear()
            self.ui.lineEdit_volumen.clear()
            self.ui.lineEdit_precio.clear()
            ##falta el else

    def editar_tinta(self):
        self.tinta_editar = self.ui.lineEdit.text()
        if self.tinta_editar != '':
            codigo = self.ui.lineEdit_codigo.text()
            color = self.ui.lineEdit_color.text()
            volumen = self.ui.lineEdit_volumen.text()
            precio = self.ui.lineEdit_precio.text()
            if codigo != '' and color != '' and volumen != '':
                self.base_datos.editar_inv(codigo, color, volumen, precio, self.tinta_editar)
                self.ui.lineEdit_codigo.clear()
                self.ui.lineEdit_color.clear()
                self.ui.lineEdit_volumen.clear()
                self.ui.lineEdit.clear()
                self.ui.lineEdit_precio.clear()
            
    def eliminar_tinta(self):
        self.tinta_borrar = self.ui.lineEdit.text()
        if self.tinta_borrar != '':
            self.base_datos.eliminar_inv("'"+ self.tinta_borrar +"'")
            self.ui.lineEdit.setText('')

class InvtintometricoTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(InvtintometricoTableModel, self).__init__(parent)
        
        # Define los nombres de las columnas
        self.columnas = ["Codigo", "Color", "Volumen", "Precio"]
        
        # Crear instancia de Database_inventario y obtener datos
        self.datos = inv_tintometrico_db().mostrar_inv() or []  # Evita el error asignando una lista vacía si es False

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