from PyQt5.QtWidgets import QMainWindow
from vistas import agregar_producto  # Importa la interfaz de la vista de inventario
from database.inventario_database import Database_inventario

class AgregarWindow(QMainWindow):
    def __init__(self):
        super(AgregarWindow, self).__init__()
        self.ui = agregar_producto.Ui_MainWindow()  # Asegúrate de usar la clase correcta
        self.ui.setupUi(self)

        #boton para agregar producto 
        self.ui.pushButton.clicked.connect(self.agregar_un_usuario)
        
    def agregar_un_usuario(self):
        nombre = self.ui.textEdit.toPlainText()
        stock= self.ui.textEdit_2.toPlainText()
        preciobase = self.ui.textEdit_3.toPlainText()
        impuesto = self.ui.textEdit_4.toPlainText()
        precio_total = self.ui.textEdit_5.toPlainText()

        self.comanda= Database_inventario() #instancia de la clase Database inventario
        self.comanda.agregar_inventario(nombre, stock,preciobase,impuesto,precio_total, "1")




    