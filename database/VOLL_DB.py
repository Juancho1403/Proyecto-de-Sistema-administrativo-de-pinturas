from .databasecomplementos import Database

class vol_tintometrico_db():
    def __init__(self):
        self.db = Database()

    def vol_act(self, volumen, codigo):
        bd = '''UPDATE venta_tintometrico SET VOLUMEN = '{}' WHERE CODIGO = '{}' '''.format(volumen, codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def sum_vol(self, volumen, codigo):
        bd = '''UPDATE venta_tintometrico SET VOLUMEN = VOLUMEN + '{}' WHERE CODIGO = '{}' '''.format(volumen, codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()
    
    def rest_vol(self, volumen, codigo):
        bd = '''UPDATE venta_tintometrico SET VOLUMEN = VOLUMEN - '{}' WHERE CODIGO = '{}' '''.format(volumen, codigo)
        self.db.cursor.execute(bd)
        self.db.connection.commit()
        self.db.cursor.close()

    def check(self, codigo):
        bd = '''SELECT COUNT(*) FROM venta_tintometrico WHERE CODIGO = '{}' '''.format(codigo)
        self.db.cursor.execute(bd)
        registro = self.db.cursor.fetchall()
        return registro