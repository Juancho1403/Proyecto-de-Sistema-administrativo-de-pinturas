from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor  # Importar QColor para establecer el color de fondo
from vistas import inventario  # Importa la interfaz de la vista de inventario
from database.inventario_database import Database_inventario
from agregar_producto_window import AgregarWindow
from modificayelimina_window import Modificayeliminaclase
from inventario_tintometrico_window import ventana_inv_tintometrico

class InventarioWindow(QMainWindow):
    def __init__(self):
        super(InventarioWindow, self).__init__()
        self.ui = inventario.InventarioWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)
        
        # Crear modelo de datos
        self.model = InventarioTableModel()
        
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)

        self.ui.pushButton.clicked.connect(self.open_inventario_agregar)
        self.ui.pushButton_2.clicked.connect(self.open_modificaryeliminar)
        self.ui.pushButton_3.clicked.connect(self.open_modificaryeliminar)
        self.ui.pushButton_4.clicked.connect(self.open_inventario_tintometrico)

    def open_inventario_agregar(self):
        self.inventario_agrega = AgregarWindow()
        self.inventario_agrega.show()
        self.close()
        
    def open_modificaryeliminar(self):
        self.inventario_elimina = Modificayeliminaclase()
        self.inventario_elimina.show()

    def open_inventario_tintometrico(self):
        self.inventario_tintometrico = ventana_inv_tintometrico()
        self.inventario_tintometrico.show()

class InventarioTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(InventarioTableModel, self).__init__(parent)
        
        # Define los nombres de las columnas
        self.columnas = ["id", "nombre", "cantidad", "precio base", "impuesto", "precio total"]
        
        # Crear instancia de Database_inventario y obtener datos
        db_inventario = Database_inventario()
        self.datos = db_inventario.todo_el_inventario() or []  # Evita el error asignando una lista vacía si es False

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
            if cantidad < 5:
                return QColor(Qt.red)  # Establecer color rojo de fondo para toda la fila
        
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            else:
                return section + 1
        return QVariant()
