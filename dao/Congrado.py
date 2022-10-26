import sqlite3
from sqlite3 import Error
from db.Conexion import Conexion


class ConGrado(Conexion):
    algo = 1
    # def __init__(self) -> None:
    #     super().__init__()

    def agregar_grado(self, grado):

        conn = self.get_connection()
        sql = """INSERT INTO grado(grado,seccion)
                  VALUES(?,?)
              """
        try:
            cursor = conn.cursor()
            cursor.execute(sql, grado)
            conn.commit()
            print("nuevo grado agregado")
            return True
        except Error as e:
            print("ERROR INGRESO grado "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def actualizar_grado(self, grado, id):
        conn = self.get_connection()
        sql = f""" UPDATE grado SET 
                        grado = ?,
                        seccion = ?
                    WHERE id_grado = {id} """
        try:
            cursor = conn.cursor()
            cursor.execute(sql, grado)
            conn.commit()
            print("grado ACTUALIZADO")
            return True
        except Error as e:
            print("ERROR ACTUALIZACION grado "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def eliminar(self, id):
        conn = self.get_connection()
        sql = f"DELETE FROM grado WHERE id_grado = {id}"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print("grado ELIMINADO")
            return True
        except Error as e:
            print("ERROR ELIMINAR grado "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_grados_combobox(self):
        conn = self.get_connection()
        sql = "SELECT  (grado||' '||seccion) AS grado  FROM grado ORDER BY grado ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            print("recargando")
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_grados(self):
        conn = self.get_connection()
        sql = "SELECT * FROM grado ORDER BY grado ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            print("recargando")
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_grados_grado_asc(self):
        conn = self.get_connection()
        sql = "SELECT * FROM grado ORDER BY grado ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_grados_seccion_asc(self):
        conn = self.get_connection()
        sql = "SELECT * FROM grado ORDER BY seccion ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def buscarGrado(self, grado):
        conn = self.get_connection()
        sql = f"SELECT * FROM grado WHERE grado LIKE '%{grado}%' OR seccion  LIKE '%{grado}%'"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def forRefresh(self):
        conn = self.get_connection()
        sql = f"SELECT * FROM grado WHERE LENGTH(grado) > 0 OR LENGTH(seccion)>0"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            grados = cursor.fetchall()
            return grados
        except Error as e:
            print("ERROR LISTAR gradoS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
