from .databasecomplementos import Database

class Database_inventario:
    def __init__(self):
        self.db = Database()

    def todo_el_inventario(self):
        """Obtiene todos los productos en el inventario."""
        try:
            query = """
                SELECT id, producto_nombre, cantidad, producto_precio_base, 
                       producto_impuesto, producto_precio_total, id_usuario 
                FROM inventario;
            """
            self.db.execute_query(query)
            results = self.db.cursor.fetchall()

            if results:
                return results
            else:
                print("No se encontraron productos en el inventario.")
                return []
        
        except Exception as e:
            print(f"Error al consultar el inventario: {e}")
            return []

    def agregar_inventario(self, nombre, cantidad, precio_base, impuesto, precio_total, id_usuario):
        """
        Agrega un nuevo producto al inventario.
        """
        try:
            query = """
                INSERT INTO inventario (producto_nombre, cantidad, producto_precio_base, 
                                        producto_impuesto, producto_precio_total, id_usuario)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            params = (nombre, cantidad, precio_base, impuesto, precio_total, id_usuario)
            self.db.execute_query(query, params)
            print("Producto agregado exitosamente al inventario.")
            return True
        
        except Exception as e:
            print(f"Error al agregar producto al inventario: {e}")
            return False

    def eliminar_inventario(self, producto_id):
        """
        Elimina un producto del inventario utilizando su ID.
        """
        try:
            query = "DELETE FROM inventario WHERE id = %s;"
            params = (producto_id,)
            self.db.execute_query(query, params)
            print("Producto eliminado exitosamente del inventario.")
            return True
        
        except Exception as e:
            print(f"Error al eliminar producto del inventario: {e}")
            return False

    def modificar_producto(self, producto_id, nombre=None, cantidad=None, precio_base=None, impuesto=None, precio_total=None, id_usuario=None):
        """
        Modifica un producto existente en el inventario.
        """
        try:
            set_clause = []
            params = []

            # Verificamos qué parámetros se han proporcionado para modificar
            if nombre is not None:
                set_clause.append("producto_nombre = %s")
                params.append(nombre)
            if cantidad is not None:
                set_clause.append("cantidad = %s")
                params.append(cantidad)
            if precio_base is not None:
                set_clause.append("producto_precio_base = %s")
                params.append(precio_base)
            if impuesto is not None:
                set_clause.append("producto_impuesto = %s")
                params.append(impuesto)
            if precio_total is not None:
                set_clause.append("producto_precio_total = %s")
                params.append(precio_total)
            if id_usuario is not None:
                set_clause.append("id_usuario = %s")
                params.append(id_usuario)

            if not set_clause:
                print("No se ha proporcionado ningún dato para modificar.")
                return False

            query = f"""
                UPDATE inventario 
                SET {', '.join(set_clause)} 
                WHERE id = %s;
            """
            params.append(producto_id)

            self.db.execute_query(query, tuple(params))
            print("Producto modificado exitosamente en el inventario.")
            return True

        except Exception as e:
            print(f"Error al modificar el producto en el inventario: {e}")
            return False