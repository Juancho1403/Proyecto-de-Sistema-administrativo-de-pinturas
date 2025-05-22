import os
import sys
import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from vistas import ventasui  # Importa la vista de la interfaz de ventas
from database.ventas_database import Database_ventas  # Clase que gestiona las ventas en la base de datos
from modificayelimina_ventas import mye_window
from agregar_ventas import agg_ventas_window

from ventas_tintometrico_window import ventana_venta_tintometrico

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ventas_window(QMainWindow):
    def __init__(self):
        super(ventas_window, self).__init__()
        self.ui = ventasui.Ui_MainWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)

        # Crear modelo de datos para ventas
        self.model = VentasTableModel()

        # Asignar el modelo a tableView de ventas
        self.ui.tableView.setModel(self.model)

        # Conectar los botones con las funciones
        self.ui.pushButton.clicked.connect(self.open_agg_ventas)
        self.ui.pushButton_2.clicked.connect(self.open_mye_ventas)
        self.ui.pushButton_3.clicked.connect(self.open_mye_ventas)
        self.ui.pushButton_4.clicked.connect(self.exportar_a_excel)

        self.ui.pushButton_6.clicked.connect(self.open_venta_tintometrico)

        self.ui.pushButton_5.clicked.connect(self.generar_factura)

    def open_mye_ventas(self):
        """Abre la ventana para modificar o eliminar ventas."""
        self.mye_ventas = mye_window()
        self.mye_ventas.show()

    def open_agg_ventas(self):
        """Abre la ventana para agregar una venta."""
        self.agg_ventas = agg_ventas_window()
        self.agg_ventas.show()

    def exportar_a_excel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Ventas"
        
        # Escribir encabezados de columna
        ws.append(self.model.columnas)
        
        # Escribir los datos
        for row in self.model.datos:
            ws.append(row)
        
        excel_file = "ventas.xlsx"
        try:
            wb.save(excel_file)
            self.show_message("Éxito", "Datos exportados a ventas.xlsx con éxito.", QMessageBox.Information)
            os.startfile(excel_file)
        except Exception as e:
            self.show_message("Error", f"No se pudo guardar el archivo: {e}", QMessageBox.Critical)

    def generar_factura(self):
        """Generar la factura de la venta seleccionada en formato PDF."""
        # Obtener el índice de la fila seleccionada
        selected_index = self.ui.tableView.selectionModel().selectedRows()
        
        if not selected_index:
            self.show_message("Error", "Por favor, seleccione una venta para generar la factura.", QMessageBox.Warning)
            return
        
        # Obtener el ID de la venta seleccionada
        row = selected_index[0].row()  # Obtener la primera fila seleccionada
        venta_id = self.model.datos[row][4]  # Suponiendo que el ID de la venta está en la columna 4 (index 4)

        # Buscar los datos de la venta correspondiente al ID
        db_ventas = Database_ventas()
        venta_data = db_ventas.obtener_venta_por_id(venta_id)

        if not venta_data:
            self.show_message("Error", "No se encontró la venta con el ID seleccionado.", QMessageBox.Warning)
            return

        # Crear el nombre del archivo PDF
        factura_file = f"factura_{venta_id}.pdf"

        # Crear el archivo PDF con ReportLab
        try:
            c = canvas.Canvas(factura_file, pagesize=letter)

            # Agregar contenido a la factura (puedes personalizar este diseño)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, f"Factura de Venta")
            c.drawString(100, 730, f"ID de Venta: {venta_data[0][4]}")
            c.drawString(100, 710, f"Cliente: {venta_data[0][1]}")
            c.drawString(100, 690, f"Producto: {venta_data[0][2]}")
            c.drawString(100, 670, f"Monto Base: {venta_data[0][3]}")
            c.drawString(100, 650, f"Monto Impuesto: {venta_data[0][5]}")
            c.drawString(100, 630, f"Monto Total: {venta_data[0][6]}")
            c.drawString(100, 610, f"Fecha: {venta_data[0][0]}")
            
            # Finalizar el PDF
            c.save()

            self.show_message("Éxito", f"Factura generada con éxito: {factura_file}", QMessageBox.Information)
            os.startfile(factura_file)  # Abrir la factura generada

        except Exception as e:
            self.show_message("Error", f"No se pudo generar la factura: {e}", QMessageBox.Critical)

    def show_message(self, title, message, icon_type):
        """Mostrar un mensaje usando QMessageBox."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon_type)
        msg_box.exec_()

    def open_venta_tintometrico(self):
        self.venta_tintometrico = ventana_venta_tintometrico()
        self.venta_tintometrico.show()

class VentasTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(VentasTableModel, self).__init__(parent)

        # Definir las columnas de acuerdo a la nueva estructura
        self.columnas = [
            "fecha", "cliente", "producto", "monto_base", "id_venta", "monto_impuesto",
            "monto_total", "forma_pago", "igtf", "usuario_id", "observaciones", "porcentaje"
        ]

        # Crear instancia de Database_ventas y obtener los datos
        db_ventas = Database_ventas()
        self.datos = db_ventas.todas_ventas() or []  # Evitar error con lista vacía si no hay datos

    def rowCount(self, parent=None):
        """Devuelve el número de filas de datos."""
        return len(self.datos)

    def columnCount(self, parent=None):
        """Devuelve el número de columnas."""
        return len(self.columnas)

    def data(self, index, role=Qt.DisplayRole):
        """Obtiene los datos para cada celda de la tabla."""
        if not index.isValid():
            return QVariant()

        # Mostrar datos en la celda
        if role == Qt.DisplayRole:
            if 0 <= index.row() < len(self.datos) and 0 <= index.column() < len(self.columnas):
                return str(self.datos[index.row()][index.column()])  # Convertir a string para Qt
        
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Devuelve los encabezados de las columnas y filas."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columnas[section]
            elif orientation == Qt.Vertical:
                return section + 1
        return QVariant()
