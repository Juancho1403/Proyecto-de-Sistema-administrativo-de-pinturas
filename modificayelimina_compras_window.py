from PyQt5.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QMessageBox, QInputDialog
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor
from vistas import modificayelimina_compra
from database.compras_database import Database_compras
import datetime


class Modificayeliminaclase_compra(QMainWindow):
    def __init__(self):
        super(Modificayeliminaclase_compra, self).__init__()
        self.ui = modificayelimina_compra.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Crear modelo de datos
        self.model = CompraTableModel()
        
        # Asignar el modelo a tableView
        self.ui.tableView.setModel(self.model)
        
        # Conectar botones a sus respectivas funciones
        self.ui.pushButton.clicked.connect(self.eliminar_compras)
        self.ui.pushButton_2.clicked.connect(self.buscar_compra)
        self.ui.pushButton_3.clicked.connect(self.modificar_compras)  # Botón para modificar

    def eliminar_compras(self):
        selected_index = self.ui.tableView.currentIndex()
        
        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un producto para eliminar.")
            return
        
        producto_id = self.model.datos[selected_index.row()][0]
        
        respuesta = QMessageBox.question(
            self, "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar el producto con ID {producto_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            db_compras = Database_compras()
            db_compras.eliminar_compra(producto_id)
            self.model.actualizar_datos()
            

    def modificar_compras(self):
        selected_index = self.ui.tableView.currentIndex()
        
        if not selected_index.isValid():
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un producto para modificar.")
            return
        
        # Obtener los datos del producto seleccionado
        datos_producto = self.model.datos[selected_index.row()]
        columnas = self.model.columnas  # Obtener nombres de columnas para claridad

        # Obtener información inicial
        valores = {
            "nombre": datos_producto[1],
            "cantidad": datos_producto[2],
            "codigo": datos_producto[3],
            "precio_base": datos_producto[4],
            "impuesto": datos_producto[5],
            "precio_total": datos_producto[6],
            "fecha": datos_producto[7],
            "detalles": datos_producto[8],
            "solicitante": datos_producto[9],
        }

        # Dialogos para actualizar cada valor
        for campo, valor in valores.items():
            nuevo_valor, ok = QInputDialog.getText(self, f"Modificar {campo.capitalize()}", f"Nuevo {campo}:", text=str(valor))
            if not ok: 
                return
            valores[campo] = nuevo_valor

        # Convertir fecha al formato correcto
        try:
            valores["fecha"] = datetime.datetime.strptime(valores["fecha"], '%Y-%m-%d').date()
        except ValueError:
            QMessageBox.warning(self, "Error", "El formato de fecha es incorrecto. Debe ser YYYY-MM-DD.")
            return

        # Actualizar datos en la base de datos
        db_compras = Database_compras()
        success = db_compras.modificar_compra(datos_producto[0], **valores)

        if success:
            QMessageBox.information(self, "Éxito", "Compra modificada exitosamente.")
            self.model.actualizar_datos()
        else:
            QMessageBox.warning(self, "Error", "Ocurrió un error al modificar la compra.")

    def buscar_compra(self):
        # Pedir el código al usuario
        codigo, ok = QInputDialog.getText(self, "Buscar Compra", "Introduce el código:")
        if not ok or not codigo:
            return

        # Buscar datos de la compra en la base de datos
        db_compras = Database_compras()
        compra = db_compras.buscar_compra_por_codigo(codigo)

        if compra:
            self.model.codigo_buscado = codigo
            self.model.datos = [compra]  # Mostrar solo la compra encontrada
            self.model.layoutChanged.emit()  # Refrescar la tabla
        else:
            QMessageBox.warning(self, "Error", "No se encontró ninguna compra con ese código.")
            self.model.codigo_buscado = None
            self.model.actualizar_datos()  # Restaurar todos los datos


class CompraTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CompraTableModel, self).__init__(parent)
        self.columnas = ["id", "producto", "cantidad", "Codigo", "precio base", "impuesto", "precio total", "Fecha", "Detalles", "Solicitante"]
        self.datos = []
        self.codigo_buscado = None  # Código buscado
        self.actualizar_datos()

    def actualizar_datos(self):
        db_compras = Database_compras()
        self.datos = db_compras.todas_compras() or []
        self.codigo_buscado = None
        self.layoutChanged.emit()

    def rowCount(self, parent=None):
        return len(self.datos)

    def columnCount(self, parent=None):
        return len(self.columnas)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        # Mostrar el valor normalmente
        if role == Qt.DisplayRole and 0 <= index.row() < len(self.datos) and 0 <= index.column() < len(self.columnas):
            return self.datos[index.row()][index.column()]

        # Resaltar la fila si coincide con el código buscado
        if role == Qt.BackgroundRole and self.codigo_buscado:
            if self.datos[index.row()][3] == self.codigo_buscado:  # Columna del código
                return QColor(Qt.yellow)  # Fondo amarillo para resaltar
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:  # Encabezados de columna
                if 0 <= section < len(self.columnas):
                    return self.columnas[section]
            elif orientation == Qt.Vertical:  # Opcional: encabezados de filas (números)
                return section + 1
        return QVariant()
