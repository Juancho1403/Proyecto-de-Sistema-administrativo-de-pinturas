from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas import login_ui  # Importa la interfaz de login

class LoginWindow(QMainWindow):
    def __init__(self, login_system, main_window_class):
        super(LoginWindow, self).__init__()
        self.ui = login_ui.Ui_Login()
        self.ui.setupUi(self)
        self.login_system = login_system
        self.main_window_class = main_window_class

        # Conecta el botón de login al método de autenticación
        self.ui.pushButton_2.clicked.connect(self.check_login)

    def check_login(self):
        usuario = self.ui.lineEdit_3.text()
        contrasena = self.ui.lineEdit_4.text()

        if self.login_system.login(usuario, contrasena):
            self.open_principal_window()
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas.")

    def open_principal_window(self):
        self.close()
        self.main_window = self.main_window_class()  # Crea una instancia de la clase principal
        self.main_window.show()
