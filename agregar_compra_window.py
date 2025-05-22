from PyQt5.QtWidgets import QMainWindow
from vistas import agregar_compra  # Asegúrate de importar correctamente la vista
from database.compras_database import Database_compras

class Agregar_compra_Window(QMainWindow):
    def __init__(self):
        super(Agregar_compra_Window, self).__init__()
        self.ui = agregar_compra.Ui_MainWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)

        # Botón para agregar Compra
        self.ui.pushButton.clicked.connect(self.agregar_una_compra)

    def agregar_una_compra(self):
        producto = self.ui.textEdit.toPlainText()
        cantidad = self.ui.textEdit_2.toPlainText()
        codigo = self.ui.textEdit_3.toPlainText()
        precio = self.ui.textEdit_4.toPlainText()
        impuesto = self.ui.textEdit_5.toPlainText()
        precio_total = self.ui.textEdit_6.toPlainText()
        
        # Obtén la fecha seleccionada correctamente
        fecha = self.ui.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        
        detalles = self.ui.textEdit_7.toPlainText()
        solicitante = self.ui.textEdit_8.toPlainText()

        # Instancia de la clase Database_compras
        self.comanda = Database_compras()
        self.comanda.agregar_compra(producto, cantidad, codigo, precio, impuesto, precio_total, fecha, detalles, solicitante)
