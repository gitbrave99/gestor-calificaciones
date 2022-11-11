import sqlite3
from sqlite3 import Error
from db.Conexion import Conexion


class ConMateria(Conexion):
    algo = 1

    def eliminar_base_datos(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            # cursor.execute("DELETE FROM materia")
            # cursor.execute("DELETE FROM grado")
            cursor.execute("DELETE FROM estudiante")
            cursor.execute("DELETE FROM calificacion")
            conn.commit()
            print("Datos borrados")
            return True
        except Error as e:
            print("ERROR ELIMINAR materia "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def agregar_materia(self, materia):

        conn = self.get_connection()
        sql = """INSERT INTO materia(materia,ciclo)
                  VALUES(?,?)
              """
        try:
            cursor = conn.cursor()
            cursor.execute(sql, materia)
            conn.commit()
            print("nuevo materia agregado")
            return True
        except Error as e:
            print("ERROR INGRESO materia "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def actualizar_materia(self, materia, id):
        conn = self.get_connection()
        sql = f""" UPDATE materia SET 
                        materia = ?,
                        ciclo= ?
                    WHERE id_materia = {id} """
        try:
            cursor = conn.cursor()
            cursor.execute(sql, materia)
            conn.commit()
            print("materia ACTUALIZADO")
            return True
        except Error as e:
            print("ERROR ACTUALIZACION materia "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def eliminar(self, id):
        conn = self.get_connection()
        sql = f"DELETE FROM materia WHERE id_materia = {id}"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print("materia ELIMINADO")
            return True
        except Error as e:
            print("ERROR ELIMINAR materia "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listarGradoSeccionIdGrado(self, grado, seccion):
        conn = self.get_connection()
        sql = f"SELECT id_grado  FROM grado WHERE grado ='{grado}' AND seccion ='{seccion}'"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            id_grado = cursor.fetchone()

            return str(id_grado)
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materias_combobox(self):
        conn = self.get_connection()
        sql = "SELECT  (materia||' '||seccion) AS materia  FROM materia ORDER BY materia ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_idMaterias_segun_ciclo(self, ciclo):
        conn = self.get_connection()
        sql = f"SELECT id_materia  FROM materia WHERE  ciclo ={ciclo} ORDER BY materia ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materias_segun_idGrado(self, ciclo):
        conn = self.get_connection()
        sql = f"SELECT *  FROM materia WHERE  ciclo ={ciclo} ORDER BY materia ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materias(self):
        conn = self.get_connection()
        sql = "SELECT * FROM materia ORDER BY materia ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materia(self):
        conn = self.get_connection()
        sql = "SELECT materia FROM materia ORDER BY materia ASC"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def listar_materia_segun_ciclo(self, id):
        conn = self.get_connection()
        sql = f"SELECT materia FROM materia WHERE ciclo ={id} ORDER BY materia ASC "
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            print("recargando")
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materias_materia_asc(self):
        conn = self.get_connection()
        sql = "SELECT * FROM materia ORDER BY materia ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def buscar_materiaGetId(self, materia):
        conn = self.get_connection()
        sql = f"SELECT id_materia FROM materia WHERE materia='{materia}'"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchone()
            return str(materias)
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_materias_seccion_asc(self):
        conn = self.get_connection()
        sql = "SELECT * FROM materia ORDER BY seccion ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def buscarmateria(self, materia):
        conn = self.get_connection()
        sql = f"SELECT * FROM materia WHERE materia LIKE '%{materia}%'"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def forRefresh(self):
        conn = self.get_connection()
        sql = f"SELECT * FROM materia WHERE LENGTH(materia) > 0 OR LENGTH(seccion)>0"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            materias = cursor.fetchall()
            return materias
        except Error as e:
            print("ERROR LISTAR materiaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
