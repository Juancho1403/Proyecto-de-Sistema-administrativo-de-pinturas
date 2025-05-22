import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from principal_window import PrincipalWindow
from database.login import Login  # Importa la clase Login para autenticación

def main():
    app = QApplication(sys.argv)
    login_system = Login()  # Instancia de autenticación
    login_window = LoginWindow(login_system, PrincipalWindow)  # Inicializa la ventana de login
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()