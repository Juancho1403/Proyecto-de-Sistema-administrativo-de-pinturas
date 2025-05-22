from .databasecomplementos import Database


class Login:
    def __init__(self):
        # Crear una instancia de la clase Database
        self.db = Database()

    def login(self, nombre, contrasena):
        try:
            # Consulta para obtener la contraseña almacenada para el usuario dado
            query = "SELECT contrasena FROM usuarios WHERE nombre = %s"
            params = (nombre,)
            result = self.db.fetch_data(query, params)

            if result:
                # Verificamos que se haya encontrado el usuario
                stored_password = result[0][0]  # Obtenemos la contraseña almacenada

                # Verificamos la contraseña ingresada comparándola con la almacenada
                if contrasena == stored_password:
                    print("Login exitoso")
                    return True
                else:
                    print("Contraseña incorrecta")
                    return False
            else:
                print("Usuario no encontrado")
                return False

        except Exception as e:
            print(f"Error durante el login: {e}")
            return False
