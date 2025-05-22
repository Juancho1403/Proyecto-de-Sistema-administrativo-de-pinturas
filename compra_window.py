import openpyxl
import os
from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import compra
from database.compras_database import Database_compras
from agregar_compra_window import Agregar_compra_Window
from modificayelimina_compras_window import Modificayeliminaclase_compra


class CompraWindow(QMainWindow):
    def __init__(self):
        super(CompraWindow, self).__init__()
        self.ui = compra.CompraWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)

        # Crear modelo de datos
        self.model = CompraTableModel()
        
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)

        self.ui.pushButton.clicked.connect(self.open_compra_agregar)
        self.ui.pushButton_2.clicked.connect(self.open_modificaryeliminar_compra)
        self.ui.pushButton_3.clicked.connect(self.open_modificaryeliminar_compra)
        self.ui.pushButton_4.clicked.connect(self.exportar_a_excel)  # Cambiar a exportar_a_excel
        
    def open_compra_agregar(self):
        self.compra_agrega = Agregar_compra_Window()  # Asegúrate de instanciar correctamente
        self.compra_agrega.show()

    def open_modificaryeliminar_compra(self):
        self.compra_elimina = Modificayeliminaclase_compra()  # Asegúrate de instanciar correctamente
        self.compra_elimina.show()

    def exportar_a_excel(self):
        # Crear un libro de trabajo y una hoja activa
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Compras"

        # Escribir encabezados de columna
        ws.append(self.model.columnas)

        # Escribir los datos de la tabla en el archivo Excel
        for row in self.model.datos:
            ws.append(row)

        # Ruta donde se guardará el archivo
        excel_file = "compras.xlsx"
        
        # Guardar el archivo Excel
        try:
            wb.save(excel_file)
            QMessageBox.information(self, "Éxito", "Datos exportados a compras.xlsx con éxito.")
            
            # Abrir el archivo Excel automáticamente
            os.startfile(excel_file)  # Abre el archivo con la aplicación predeterminada (usualmente Excel)
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")


class CompraTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CompraTableModel, self).__init__(parent)
        
        # Define los nombres de las columnas
        self.columnas = ["id", "producto", "cantidad", "Codigo", "precio base", "impuesto", "precio total", "Fecha", "Detalles", "Solicitante"]
        
        # Crear instancia de Database_compras y obtener datos
        db_compras = Database_compras()
        self.datos = db_compras.todas_compras() or []  # Llama al método correctamente

    def rowCount(self, parent=None):
        return len(self.datos)

    def columnCount(self, parent=None):
        return len(self.columnas)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        
        # Mostrar datos en la celda
        if role == Qt.DisplayRole:
            if 0 <= index.row() < len(self.datos) and 0 <= index.column() < len(self.columnas):
                return self.datos[index.row()][index.column()]

        # Cambiar el color de fondo si la cantidad es menor a 5
        if role == Qt.BackgroundRole:
            cantidad = self.datos[index.row()][2]  # Asume que la columna "cantidad" es la tercera
            
            # Convertir cantidad a int si es necesario
            try:
                cantidad_num = int(cantidad)  # Intenta convertir a entero
            except (ValueError, TypeError):  # Manejar ValueError y TypeError
                cantidad_num = 0  # Si no se puede convertir, asigna un valor por defecto
            
            if cantidad_num < 5:
                return QVariant(Qt.yellow)  # Cambiar el color de fondo a amarillo si cantidad es menor a 5
        
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            else:
                return section + 1
        return QVariant()
