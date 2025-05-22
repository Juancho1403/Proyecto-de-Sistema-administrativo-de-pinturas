from .databasecomplementos import Database

class venta_tintometrico_db():
    def __init__(self):
        self.db = Database()

    def agregar_tablaventa(self, codigo):
        bd = '''INSERT INTO venta_tintometrico SELECT * FROM inventario_tintometrico WHERE CODIGO = '{}' '''.format(codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()