from .databasecomplementos import Database

class inv_tintometrico_db():
    def __init__(self):
        self.db = Database()

    def mostrar_inv(self):
        bd = "SELECT * FROM inventario_tintometrico"
        self.db.cursor.execute(bd)
        registro = self.db.cursor.fetchall()
        return registro

    def agregar_inv(self, codigo, color, volumen, precio):
        bd = '''INSERT INTO inventario_tintometrico(CODIGO, COLOR, VOLUMEN, PRECIO)
        VALUES('{}','{}','{}', '{}')'''.format(codigo, color, volumen, precio) #cambiar nombre de tabla usuarios y de los atirbutos
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def eliminar_inv(self, codigo):
        bd = '''DELETE FROM inventario_tintometrico WHERE CODIGO = '{}' '''.format(codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def editar_inv(self, codigo, color, volumen, precio, codigo_i):
        bd = '''UPDATE inventario_tintometrico SET CODIGO = '{}', COLOR = '{}', VOLUMEN = '{}', PRECIO_CC = '{}'
        WHERE CODIGO = '{}' '''.format(codigo, color, volumen, precio, codigo_i)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def restar_vol_inv(self, codigo, volumen):
        bd = '''UPDATE inventario_tintometrico SET VOLUMEN = VOLUMEN - '{}' WHERE CODIGO = '{}' '''.format(volumen, codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def sumar_vol_inv(self, codigo, volumen):
        bd = '''UPDATE inventario_tintometrico SET VOLUMEN = VOLUMEN + '{}' WHERE CODIGO = '{}' '''.format(volumen, codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()
        
    def mostrar_venta(self):
        bd = "SELECT * FROM venta_tintometrico"
        self.db.cursor.execute(bd)
        registro = self.db.cursor.fetchall()
        return registro