from PyQt5.QtWidgets import QMainWindow
from vistas import principal_ui  # Importa la interfaz de la ventana principal
from inventario_window import InventarioWindow  # Importa la clase InventarioWindow
from compra_window import CompraWindow  # Importar la clase de compras
from USUARIOS import ventana_usuario
from ventana_ventas import ventas_window

class PrincipalWindow(QMainWindow):
    def __init__(self):
        super(PrincipalWindow, self).__init__()
        self.ui = principal_ui.Ui_Principal()
        self.ui.setupUi(self)

        # Conectar botones a sus respectivos métodos
        self.ui.pushButton_3.clicked.connect(self.open_inventario_window)
        self.ui.pushButton.clicked.connect(self.open_compras)
        self.ui.pushButton_2.clicked.connect(self.open_ventas)
        self.ui.pushButton_5.clicked.connect(self.open_usuarios)
        self.ui.pushButton_6.clicked.connect(self.close_window)

    def open_inventario_window(self):
        # Crear una instancia de InventarioWindow y mostrarla
        self.inventario_window = InventarioWindow()
        self.inventario_window.show()

    def open_compras(self):
        # Crear una instancia de CompraWindow y mostrarla
        self.compra_window = CompraWindow()
        self.compra_window.show()

    def open_usuarios(self):
        # Crear una instancia de ventana_usuario y mostrarla
        self.usuario_window = ventana_usuario()
        self.usuario_window.show()

    def open_ventas(self):
        # Crear una instancia de ventas_window y mostrarla
        self.ventas_window = ventas_window()
        self.ventas_window.show()

    def close_window(self):
        # Cerrar la ventana principal
        self.close()


