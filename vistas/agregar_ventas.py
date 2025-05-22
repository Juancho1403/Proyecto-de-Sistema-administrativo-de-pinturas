from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas import agregar_ventasui  # Asegúrate de importar correctamente la vista
from database.ventas_database import Database_ventas

class agg_ventas_window(QMainWindow):
    def __init__(self):
        super(agg_ventas_window, self).__init__()
        self.ui = agregar_ventasui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Botón para agregar Venta
        self.ui.pushButton.clicked.connect(self.agregar_una_venta)

    def agregar_una_venta(self):
        # Obtén los valores de los campos de la interfaz
        fecha = self.ui.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        cliente = self.ui.textEdit.toPlainText()
        monto_base = self.ui.textEdit_2.toPlainText()
        monto_impuesto = self.ui.textEdit_3.toPlainText()
        monto_total = self.ui.textEdit_4.toPlainText()  # Asegúrate de solo tomar un valor para monto_total
        forma_pago = self.ui.textEdit_5.toPlainText()
        igtf = self.ui.textEdit_7.toPlainText()
        observaciones = self.ui.textEdit_8.toPlainText()
        porcentaje = self.ui.textEdit_9.toPlainText() or "0"  # Asigna "0" si el campo está vacío
        nombre_producto = self.ui.textEdit_10.toPlainText() 

        # Verifica que todos los campos obligatorios estén completos
        if not fecha or not cliente or not monto_base or not monto_impuesto or not monto_total or not forma_pago:
            self.show_message("Error", "Todos los campos obligatorios deben ser llenados.", QMessageBox.Critical)
            return
        
        # Instancia de la clase Database_ventas
        self.comanda = Database_ventas()

        # Asegúrate de que el método agregar_venta reciba correctamente todos los parámetros
        try:
            # Llamada al método para agregar la venta
            self.comanda.agregar_venta(fecha, cliente, monto_base, monto_impuesto, monto_total, 
                                        forma_pago, igtf, observaciones, porcentaje, nombre_producto)
            # Si se agrega con éxito, muestra un mensaje de éxito
            self.show_message("Éxito", "Venta agregada correctamente.", QMessageBox.Information)
        except Exception as e:
            # Si hay algún error, muestra un mensaje de error
            self.show_message("Error", f"No se pudo agregar la venta: {e}", QMessageBox.Critical)

    def show_message(self, title, message, icon_type):
        """Mostrar un mensaje usando QMessageBox."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon_type)
        msg_box.exec_()
