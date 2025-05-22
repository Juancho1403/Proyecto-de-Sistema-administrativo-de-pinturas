import mysql.connector

class Database:
    def __init__(self):
        # Conectar a la base de datos
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sistema_de_programas',
            port='3306',
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        # Ejecutar una consulta SQL
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        
        # Solo liberar resultados pendientes para consultas de escritura, cuando el commit es necesario
        if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
            # Liberar resultados pendientes solo en operaciones de escritura
            while self.cursor.nextset():
                pass
            self.connection.commit()


    def fetch_data(self, query, params=None):
        # Obtener datos de una consulta SQL
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()