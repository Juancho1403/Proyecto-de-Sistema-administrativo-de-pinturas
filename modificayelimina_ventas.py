import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget, QMessageBox, QInputDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import modificayelimina_ventasui
from database.ventas_database import Database_ventas

class mye_window(QMainWindow):
    def __init__(self):
        super(mye_window, self).__init__()
        self.ui = modificayelimina_ventasui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Crear modelo de datos
        self.model = VentasTableModel()
        
        # Asignar el modelo al QTableView
        self.ui.tableView.setModel(self.model)

        # Conectar los botones con las respectivas funciones
        self.ui.pushButton.clicked.connect(self.eliminar_venta)
        self.ui.pushButton_2.clicked.connect(self.buscar_venta)
        self.ui.pushButton_3.clicked.connect(self.modificar_venta)

    def eliminar_venta(self):
        """Eliminar una venta seleccionada en la tabla."""
        selected_index = self.ui.tableView.currentIndex()
        
        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una venta para eliminar.")
            return

        # Obtener el id de la venta seleccionada (ahora está en la columna 3)
        id_venta = self.model.datos[selected_index.row()][3]  # id_venta está en la columna 3
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación", 
            f"¿Estás seguro de que deseas eliminar la venta con ID {id_venta}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            db_ventas = Database_ventas()
            success = db_ventas.eliminar_venta(id_venta)
            if success:
                self.model.actualizar_datos()
                QMessageBox.information(self, "Éxito", "Venta eliminada correctamente.")
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar la venta.")

    def buscar_venta(self):
        """Buscar una venta por ID."""
        id_venta, ok = QInputDialog.getText(self, "Buscar Venta", "Introduce el ID de la venta:")
        if not ok or not id_venta:
            return

        # Buscar la venta en la base de datos
        db_ventas = Database_ventas()
        venta = db_ventas.buscar_venta_por_id(id_venta)

        if venta:
            self.model.datos = [venta]  # Solo mostrar la venta encontrada
            self.model.layoutChanged.emit()  # Refrescar la tabla
        else:
            QMessageBox.warning(self, "No Encontrado", f"No se encontró una venta con ID {id_venta}.")
            self.model.actualizar_datos()  # Restaurar todos los datos si no se encuentra

    def modificar_venta(self):
        """Modificar una venta seleccionada en la tabla."""
        selected_index = self.ui.tableView.currentIndex()
        
        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una venta para modificar.")
            return

        # Obtener los datos de la venta seleccionada
        datos_venta = self.model.datos[selected_index.row()]
        
        # Obtener los valores actuales de la venta
        valores = {
            "fecha": datos_venta[0],
            "cliente": datos_venta[1],
            "producto": datos_venta[2],  # Añadir producto
            "monto_base": datos_venta[3],
            "id_venta": datos_venta[4],  # El id_venta está en la columna 4
            "monto_impuesto": datos_venta[5],
            "monto_total": datos_venta[6],
            "forma_pago": datos_venta[7],
            "igtf": datos_venta[8],
            "usuario_id": datos_venta[9],
            "observaciones": datos_venta[10],
            "porcentaje": datos_venta[11],
        }

        # Usamos QInputDialog para modificar los valores de cada campo
        for campo, valor in valores.items():
            nuevo_valor, ok = QInputDialog.getText(self, f"Modificar {campo.capitalize()}", f"Nuevo valor para {campo}:", text=str(valor))
            if not ok:
                return
            valores[campo] = nuevo_valor

        # Ahora pasamos todos los valores directamente, sin necesidad de pasar 'id_venta' explícitamente
        db_ventas = Database_ventas()
        success = db_ventas.modificar_venta(**valores)

        if success:
            self.model.actualizar_datos()
            QMessageBox.information(self, "Éxito", "Venta modificada correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar la venta.")

class VentasTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(VentasTableModel, self).__init__(parent)
        
        self.columnas = [
            "fecha", "cliente", "producto", "monto_base", "id_venta", "monto_impuesto",
            "monto_total", "forma_pago", "igtf", "usuario_id", "observaciones", "porcentaje"
        ]
        
        self.datos = []
        self.actualizar_datos()

    def actualizar_datos(self):
        """Actualizar los datos de la tabla con las ventas desde la base de datos."""
        db_ventas = Database_ventas()
        self.datos = db_ventas.todas_ventas() or []
        self.layoutChanged.emit()

    def rowCount(self, parent=None):
        """Número de filas (ventas)."""
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

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Encabezados de columna y fila."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            elif orientation == Qt.Vertical:
                return section + 1
        return QVariant()
