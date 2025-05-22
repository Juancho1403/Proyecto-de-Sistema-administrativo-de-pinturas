from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QMessageBox, QInputDialog
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor
from vistas import modificayelimina  # Importar la interfaz de la vista de inventario
from database.inventario_database import Database_inventario

class Modificayeliminaclase(QMainWindow):
    def __init__(self):
        super(Modificayeliminaclase, self).__init__()
        self.ui = modificayelimina.Ui_MainWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)
        
        # Crear modelo de datos
        self.model = InventarioTableModel()
        
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)
        
        # Conectar botones a funciones correspondientes
        self.ui.pushButton.clicked.connect(self.eliminar_producto)
        self.ui.pushButton_2.clicked.connect(self.buscar_producto)
        self.ui.pushButton_3.clicked.connect(self.modificar_producto)

    def eliminar_producto(self):
        """Eliminar un producto seleccionado en la tabla."""
        selected_index = self.ui.tableView.currentIndex()
        
        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un producto para eliminar.")
            return
        
        # Obtener el ID del producto seleccionado
        producto_id = self.model.datos[selected_index.row()][0]  # Suponiendo que la ID está en la primera columna
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación", 
            f"¿Estás seguro de que deseas eliminar el producto con ID {producto_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            db_inventario = Database_inventario()
            db_inventario.eliminar_inventario(producto_id)
            self.model.actualizar_datos()
            QMessageBox.information(self, "Éxito", "Producto eliminado correctamente.")

    def buscar_producto(self):
        """Buscar un producto por ID."""
        producto_id, ok = QInputDialog.getText(self, "Buscar Producto", "Introduce el ID del producto:")
        if not ok or not producto_id:
            return

        # Buscar el producto en la base de datos
        db_inventario = Database_inventario()
        producto = db_inventario.buscar_producto_por_id(producto_id)

        if producto:
            self.model.datos = [producto]  # Mostrar solo el producto encontrado
            self.model.layoutChanged.emit()  # Refrescar la tabla
        else:
            QMessageBox.warning(self, "No Encontrado", f"No se encontró un producto con ID {producto_id}.")
            self.model.actualizar_datos()  # Restaurar todos los productos si no se encuentra

    def modificar_producto(self):
        """Modificar un producto seleccionado en la tabla."""
        selected_index = self.ui.tableView.currentIndex()

        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un producto para modificar.")
            return

        # Obtener los datos del producto seleccionado
        datos_producto = self.model.datos[selected_index.row()]

        # Obtener los valores actuales del producto
        valores = {
            "producto_id": datos_producto[0],  # Cambiar 'id_producto' a 'producto_id'
            "nombre": datos_producto[1],
            "cantidad": datos_producto[2],
            "precio_base": datos_producto[3],
            "impuesto": datos_producto[4],
            "precio_total": datos_producto[5],
        }

        # Usamos QInputDialog para modificar los valores de cada campo
        for campo, valor in valores.items():
            nuevo_valor, ok = QInputDialog.getText(self, f"Modificar {campo.capitalize()}", f"Nuevo valor para {campo}:", text=str(valor))
            if not ok:
                return
            valores[campo] = nuevo_valor

        # Pasar los nuevos valores al modelo de base de datos
        db_inventario = Database_inventario()
        success = db_inventario.modificar_producto(**valores)

        if success:
            self.model.actualizar_datos()
            QMessageBox.information(self, "Éxito", "Producto modificado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar el producto.")


class InventarioTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(InventarioTableModel, self).__init__(parent)
        
        self.columnas = ["id", "nombre", "cantidad", "precio base", "impuesto", "precio total"]
        
        self.datos = []
        self.actualizar_datos()

    def actualizar_datos(self):
        """Actualizar los datos de la tabla con el inventario desde la base de datos."""
        db_inventario = Database_inventario()
        self.datos = db_inventario.todo_el_inventario() or []
        self.layoutChanged.emit()

    def rowCount(self, parent=None):
        """Número de filas (productos)."""
        return len(self.datos)

    def columnCount(self, parent=None):
        """Número de columnas.""" 
        return len(self.columnas)

    def data(self, index, role=Qt.DisplayRole):
        """Obtener los datos de cada celda."""
        if not index.isValid():
            return QVariant()

        if role == Qt.DisplayRole:
            if 0 <= index.row() < len(self.datos) and 0 <= index.column() < len(self.columnas):
                return str(self.datos[index.row()][index.column()])

        # Cambiar el color de fondo si la cantidad es menor a 5
        if role == Qt.BackgroundRole:
            cantidad = self.datos[index.row()][2]  # Asume que la columna "cantidad" es la tercera
            if cantidad < 5:
                return QColor(Qt.red)  # Establecer color rojo de fondo para toda la fila
        
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Encabezados de columna y fila."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            elif orientation == Qt.Vertical:
                return section + 1
        return QVariant()
