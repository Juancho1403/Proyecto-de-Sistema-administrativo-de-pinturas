import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from database.usuarios_database import usuario_db
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import USERSui

class ventana_usuario(QMainWindow):
    def __init__(self):
        super(ventana_usuario, self).__init__()
        self.ui = USERSui.Ui_Form()
        self.ui.setupUi(self)

        self.base_datos = usuario_db()

        self.ui.Create_Buttom.clicked.connect(self.crear_usuari0)
        self.ui.Edit_Buttom.clicked.connect(self.editar_usuari0)
        self.ui.Eliminate_Buttom.clicked.connect(self.eliminar_usuari0)

        # Crear modelo de datos
        self.model = UsuariosTableModel()
            
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)

    def crear_usuari0(self):
        id = self.ui.textEdit_ID.text().upper()
        nombres = self.ui.textEdit_Nombres.text().upper()
        apellidos = self.ui.textEdit_Apellidos.text().upper()
        email = self.ui.textEdit_email.text().upper()
        telefono = self.ui.textEdit_Telefono.text().upper()
        if id != '' and nombres != '' and apellidos != '' and email != '' and telefono != '':
            self.base_datos.crear_usuario(id, nombres, apellidos, email, telefono)
            self.ui.textEdit_ID.clear()
            self.ui.textEdit_Nombres.clear()
            self.ui.textEdit_Apellidos.clear()
            self.ui.textEdit_email.clear()
            self.ui.textEdit_Telefono.clear()
            ##falta el else

    def editar_usuari0(self):
        self.usuario_editar = self.ui.textEdit_Buscar.text().upper()
        if self.usuario_editar != '':
            id = self.ui.textEdit_ID.text().upper()
            nombres = self.ui.textEdit_Nombres.text().upper()
            apellidos = self.ui.textEdit_Apellidos.text().upper()
            email = self.ui.textEdit_email.text().upper()
            telefono = self.ui.textEdit_Telefono.text().upper()
            if id != '' and nombres != '' and apellidos != '' and email != '' and telefono != '':
                self.base_datos.editar_usuario(id, nombres, apellidos, email, telefono, self.usuario_editar)
                self.ui.textEdit_ID.clear()
                self.ui.textEdit_Nombres.clear()
                self.ui.textEdit_Apellidos.clear()
                self.ui.textEdit_email.clear()
                self.ui.textEdit_Telefono.clear()
                self.ui.textEdit_Buscar.clear()
            
    def eliminar_usuari0(self):
        self.usuario_borrar = self.ui.textEdit_Buscar.text().upper()
        if self.usuario_borrar != '':   #self.usuario_editar
            self.base_datos.eliminar_usuario("'"+ self.usuario_borrar +"'")
            self.ui.textEdit_Buscar.setText('')

class UsuariosTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(UsuariosTableModel, self).__init__(parent)
        
        # Define los nombres de las columnas
        self.columnas = ["ID", "Nombres", "Clave", "e-mail", "Telefono"]
        
        # Crear instancia de Database_inventario y obtener datos
        self.datos = usuario_db().mostrar_usuario() or []  # Evita el error asignando una lista vacía si es False

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