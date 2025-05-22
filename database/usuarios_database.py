from .databasecomplementos import Database

class usuario_db():
    def __init__(self):
        self.db = Database()

    def mostrar_usuario(self):
        bd = "SELECT * FROM usuarios"
        self.db.cursor.execute(bd)
        registro = self.db.cursor.fetchall()
        return registro

    def crear_usuario(self, id, nombres, contrasena, email, telefono):
        bd = '''INSERT INTO usuarios(ID, NOMBRE, CONTRASENA, EMAIL, TELEFONO)
        VALUES('{}','{}','{}','{}','{}')'''.format(id, nombres, contrasena, email, telefono) #cambiar nombre de tabla usuarios y de los atirbutos
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def eliminar_usuario(self, nombre):
        bd = '''DELETE FROM usuarios WHERE NOMBRE = {}'''.format(nombre)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def editar_usuario(self, id, nombres, contrasena, email, telefono, nombres_i):
        bd = '''UPDATE usuarios SET ID = '{}', NOMBRE = '{}', CONTRASENA = '{}', EMAIL = '{}', TELEFONO = '{}'
        WHERE NOMBRE = '{}' '''.format(id, nombres, contrasena, email, telefono, nombres_i)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()