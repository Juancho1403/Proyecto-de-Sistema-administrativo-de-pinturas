from .databasecomplementos import Database

class Database_compras:
    def __init__(self):
        # Crear una instancia de la clase Database
        self.db = Database()

    def todas_compras(self):
        try:
            # Consulta para obtener todos los productos de las compras
            query = "SELECT * FROM compras;"
            self.db.execute_query(query)
            
            # Obtener todos los resultados de la consulta
            results = self.db.cursor.fetchall()  # Usar el cursor de self.db
            
            if results:
                print("Datos encontrados:", results)
            else:
                print("No se encontraron datos de la compra.")
            
            return results
        
        except Exception as e:
            print(f"Error al consultar el módulo de compras: {e}")
            return []

    def agregar_compra(self, nombre, cantidad, codigo, precio_base, impuesto, precio_total, fecha, detalles, solicitante):
        """
        Agrega una nueva compra.
        """
        try:
            # Consulta para insertar una nueva compra
            query = """
                INSERT INTO compras (producto, cantidad, codigo, 
                                    precio_base, impuesto, precio_total, 
                                    fecha, detalles, solicitante)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            params = (nombre, cantidad, codigo, precio_base, impuesto, precio_total, fecha, detalles, solicitante)
            self.db.execute_query(query, params)  # Asegúrate de que execute_query acepta estos parámetros
            print("Compra agregada exitosamente a la tabla.")
            return True
        
        except Exception as e:
            print(f"Error al agregar una nueva compra: {e}")
            return False        
    
    def eliminar_compra(self, producto_id):
        """
        Elimina una compra solo usando el ID del producto.
        """
        try:
            # Consulta para eliminar una compra usando solo el producto_id
            query = "DELETE FROM compras WHERE id = %s;"
            params = (producto_id,)
            self.db.execute_query(query, params)
            print("Compra eliminada exitosamente.")
            return True

        except Exception as e:
            print(f"Error al eliminar una compra: {e}")
            return False
    
    def modificar_compra(self, producto_id, nombre=None, cantidad=None, codigo=None, precio_base=None, 
                         impuesto=None, precio_total=None, fecha=None, detalles=None, solicitante=None):
        """
        Modifica los detalles de una compra existente.
        Los parámetros opcionales pueden ser enviados para actualizar solo ciertos campos.
        """
        try:
            # Crear la consulta de actualización dinámica
            set_clause = []
            params = []

            if nombre is not None:
                set_clause.append("producto = %s")
                params.append(nombre)
            if cantidad is not None:
                set_clause.append("cantidad = %s")
                params.append(cantidad)
            if codigo is not None:
                set_clause.append("codigo = %s")
                params.append(codigo)
            if precio_base is not None:
                set_clause.append("precio_base = %s")
                params.append(precio_base)
            if impuesto is not None:
                set_clause.append("impuesto = %s")
                params.append(impuesto)
            if precio_total is not None:
                set_clause.append("precio_total = %s")
                params.append(precio_total)
            if fecha is not None:
                set_clause.append("fecha = %s")
                params.append(fecha)
            if detalles is not None:
                set_clause.append("detalles = %s")
                params.append(detalles)
            if solicitante is not None:
                set_clause.append("solicitante = %s")
                params.append(solicitante)

            # Si no se ha pasado ningún campo para actualizar, lanzar una excepción
            if not set_clause:
                print("No se ha proporcionado ningún dato para modificar.")
                return False

            # Agregar la condición para actualizar la compra por su ID
            query = f"""
                UPDATE compras 
                SET {', '.join(set_clause)} 
                WHERE id = %s;
            """
            params.append(producto_id)  # Agregar el id del producto a los parámetros

            self.db.execute_query(query, tuple(params))  # Ejecutar la consulta
            print("Compra modificada exitosamente.")
            return True
        
        except Exception as e:
            print(f"Error al modificar la compra: {e}")
            return False
    
    def buscar_compra_por_codigo(self, codigo):
        try:
            # Consulta SQL para buscar una compra por el código
            query = "SELECT * FROM compras WHERE codigo = %s;"
            params = (codigo,)
            self.db.execute_query(query, params)
            result = self.db.cursor.fetchone()  # Obtener un solo resultado
            
            if result:
                print(f"Compra encontrada: {result}")
                return result
            else:
                print("No se encontró ninguna compra con ese código.")
                return None
        except Exception as e:
            print(f"Error al buscar la compra: {e}")
            return None
    

   
