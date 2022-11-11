import sqlite3
from sqlite3 import Error
from db.Conexion import Conexion


class ConEstudiante(Conexion):

    def agregar_estudiante(self, estudiante):
        conn = self.get_connection()
        sql = """ INSERT INTO estudiante(nombre,nie,id_grado)
                  VALUES(?,?,?)
        """
        try:
            cursor = conn.cursor()
            cursor.execute(sql, estudiante)
            conn.commit()
            print("nuevo estudiante agregado")
            return True
        except Error as e:
            print("ERROR INGRESO ESTUDIANTE "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()


    def actualizar_estudiante(self,estudiante,id):
        conn = self.get_connection()
        sql = f""" UPDATE estudiante SET 
                        nombre = ?, nie = ?, id_grado = ? WHERE id_estudiante = {id}"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql,estudiante)
            conn.commit()
            print("ESTUDIANTE ACTUALIZADO")
            return True
        except Error as e:
            print("ERROR ACTUALIZACION ESTUDIANTE "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def eliminar(self,id):
        conn = self.get_connection()
        sql = f"DELETE FROM estudiante WHERE id_estudiante = {id}"
        
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print("ESTUDIANTE ELIMINADO")
            return True
        except Error as e:
            print("ERROR ELIMINAR ESTUDIANTE "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def listar_estudiantes_segun_grado(self,idgrado):
        conn = self.get_connection()
        sql = f"SELECT * FROM estudiante WHERE id_grado={idgrado}"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchall()
            return estudiantes
        except Error as e:
            print("ERROR LISTAR ESTUDIANTES "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_estudiantes(self):
        conn = self.get_connection()
        sql = "SELECT * FROM estudiante"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchall()
            return estudiantes
        except Error as e:
            print("ERROR LISTAR ESTUDIANTES "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    #OBTENER ULTIMO ESTUDIANTE INSERTADO
    def obtener_ultimo_estudiante_insertado(self):
        conn = self.get_connection()
        sql = "SELECT MAX(id_estudiante) FROM estudiante e"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchone()
            return str(estudiantes)
        except Error as e:
            print("ERROR LISTAR ESTUDIANTES "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def listar_estudiantes_nombre_asc_byIdGrado(self,id):
        conn = self.get_connection()
        sql = f"SELECT * FROM estudiante WHERE id_grado={id} ORDER BY nombre ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchall()
            return estudiantes
        except Error as e:
            print("ERROR LISTAR ESTUDIANTES "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def listar_estudiantes_nombre_nie_asc_byIdGrado(self,id):
        conn = self.get_connection()
        sql = f"SELECT * FROM estudiante WHERE id_grado={id} ORDER BY nie ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchall()
            return estudiantes
        except Error as e:
            print("ERROR LISTAR ESTUDIANTES "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def buscarEstudiante(self,estudiante,idGrado):
        conn = self.get_connection()
        sql = f"SELECT * FROM estudiante WHERE id_grado = {idGrado} AND (nombre LIKE '%{estudiante}%' OR nie  LIKE '%{estudiante}%')"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            estudiantes = cursor.fetchall()
            return estudiantes
        except Error as e:
            print("ERROR busqueda estudiantes "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()