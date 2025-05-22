from .databasecomplementos import Database

class Database_ventas:
    def __init__(self):
        self.db = Database()

    def todas_ventas(self):
        try:
            query = """
                SELECT fecha, cliente, producto, monto_base, id_venta, monto_impuesto, monto_total, forma_pago, igtf, usuario_id, observaciones, porcentaje 
                FROM ventas;
            """
            self.db.execute_query(query)
            results = self.db.cursor.fetchall()

            if results:
                return results
            else:
                print("No se encontraron datos de la venta.")
                return []
        
        except Exception as e:
            print(f"Error al consultar el módulo de ventas: {e}")
            return []

    def agregar_venta(self, fecha, cliente, producto, monto_base, monto_impuesto, monto_total, forma_pago, igtf, observaciones, porcentaje):
        """
        Agrega una nueva venta.
        """
        try:
            # Aquí el id_venta debe ser autoincremental, por lo tanto no lo pasamos como parámetro.
            query = """
                INSERT INTO ventas (fecha, cliente, producto, monto_base, monto_impuesto, monto_total, forma_pago, igtf, observaciones, porcentaje)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            params = (fecha, cliente, producto, monto_base, monto_impuesto, monto_total, forma_pago, igtf, observaciones, porcentaje)
            self.db.execute_query(query, params)
            print("Venta agregada exitosamente a la tabla.")
            return True
        
        except Exception as e:
            print(f"Error al agregar una nueva venta: {e}")
            return False        

    def eliminar_venta(self, id_venta):
        try:
            query = "DELETE FROM ventas WHERE id_venta = %s;"
            params = (id_venta,)
            self.db.execute_query(query, params)
            print("Venta eliminada exitosamente.")
            return True

        except Exception as e:
            print(f"Error al eliminar una venta: {e}")
            return False
    
    def modificar_venta(self, id_venta, fecha=None, cliente=None, producto=None, monto_base=None, monto_impuesto=None, monto_total=None, forma_pago=None, igtf=None, usuario_id=None, observaciones=None, porcentaje=None):
        try:
            set_clause = []
            params = []

            if fecha is not None:
                set_clause.append("fecha = %s")
                params.append(fecha)
            if cliente is not None:
                set_clause.append("cliente = %s")
                params.append(cliente)
            if producto is not None:
                set_clause.append("producto = %s")
                params.append(producto)
            if monto_base is not None:
                set_clause.append("monto_base = %s")
                params.append(monto_base)
            if monto_impuesto is not None:
                set_clause.append("monto_impuesto = %s")
                params.append(monto_impuesto)
            if monto_total is not None:
                set_clause.append("monto_total = %s")
                params.append(monto_total)
            if forma_pago is not None:
                set_clause.append("forma_pago = %s")
                params.append(forma_pago)
            if igtf is not None:
                set_clause.append("igtf = %s")
                params.append(igtf)
            if usuario_id is not None:
                set_clause.append("usuario_id = %s")
                params.append(usuario_id)
            if observaciones is not None:
                set_clause.append("observaciones = %s")
                params.append(observaciones)
            if porcentaje is not None:
                set_clause.append("porcentaje = %s")
                params.append(porcentaje)

            if not set_clause:
                print("No se ha proporcionado ningún dato para modificar.")
                return False

            query = f"""
                UPDATE ventas 
                SET {', '.join(set_clause)} 
                WHERE id_venta = %s;
            """
            params.append(id_venta)  
            self.db.execute_query(query, tuple(params))
            print("Venta modificada exitosamente.")
            return True
        
        except Exception as e:
            print(f"Error al modificar la venta: {e}")
            return False

    def buscar_venta_por_id(self, id_venta):
        """Buscar una venta por ID."""
        try:
            query = "SELECT * FROM ventas WHERE id_venta = %s;"
            params = (id_venta,)
            self.db.execute_query(query, params)
            result = self.db.cursor.fetchone()
            return result
        
        except Exception as e:
            print(f"Error al buscar la venta: {e}")
            return None
        
    def obtener_venta_por_id(self, venta_id):
        try:
            query = f"SELECT * FROM ventas WHERE id_venta = {venta_id}"
            self.db.execute_query(query)
            result = self.db.cursor.fetchone()  # Obtener solo una fila

            if result:
                return [result]
            else:
                return None
        except Exception as e:
            print(f"Error al obtener los datos de la venta: {e}")
            return None
