import sqlite3
from sqlite3 import Error
from db.Conexion import Conexion


class ConNotas(Conexion):

    def crearDefault_notaTercerCiclo(self, nota):
        conn = self.get_connection()
        sql = """INSERT INTO calificacion (act1,act2,act3,no_periodo,id_estudiante,id_materia)
                VALUES(?,?,?,?,?,?)"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql, nota)
            conn.commit()
            print("calficacion agregada")
            return True
        except Error as e:
            print("ERROR INGRESO nota "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def actualizar_notaTercerCiclo(self, nota, idCalificacion):
        conn = self.get_connection()
        sql = f"UPDATE calificacion SET act1=?,act2=?,act3=? WHERE id_calificacion={idCalificacion}"
        try:
            cursor = conn.cursor()
            cursor.execute(sql, nota)
            conn.commit()
            return True
        except Error as e:
            print("ERROR INGRESO nota "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def actualizar_nota(self, nota, id):
        conn = self.get_connection()
        sql = f""" UPDATE nota SET
                        nombre = ?, nie = ?, id_grado = ? WHERE id_nota = {id}"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql, nota)
            conn.commit()
            print("nota ACTUALIZADO")
            return True
        except Error as e:
            print("ERROR ACTUALIZACION nota "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def eliminar(self, idCalificacion):
        conn = self.get_connection()
        nota = (0, 0, 0)
        sql = f"UPDATE calificacion SET act1=?,act2=?,act3=? WHERE id_calificacion={idCalificacion}"
        try:
            cursor = conn.cursor()
            cursor.execute(sql, nota)
            conn.commit()
            print("nota ELIMINADO")
            return True
        except Error as e:
            print("ERROR ELIMINAR nota "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_calificaciones_segun_periodo(self, periodo):
        conn = self.get_connection()
        sql = f"""SELECT c.id_calificacion,e.nombre ,c.act1,c.act2,c.act3,c.act4 FROM calificacion c
                   INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                   INNER JOIN materia m ON c.id_materia = m.id_materia
                   WHERE c.no_periodo ='{periodo}'  """
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_calificaciones_segun_idGrado_periodo(self, idGrado, periodo):
        conn = self.get_connection()
        sql = f"""SELECT c.id_calificacion,e.nombre ,c.act1,c.act2,c.act3,c.act4 FROM calificacion c
                   INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                   INNER JOIN grado g  ON e.id_grado  = g.id_grado
                   INNER JOIN materia m ON c.id_materia = m.id_materia
                   WHERE c.no_periodo ='{periodo}' AND g.id_grado = {idGrado} """
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_calificaciones_segun_idGrado_periodo_materia(self, idGrado, periodo, materia):
        conn = self.get_connection()
        sql = f"""SELECT c.id_calificacion,e.id_estudiante, e.nombre ,c.act1, ROUND((c.act1*0.35),2), c.act2,ROUND((c.act1*0.35),2),c.act3,ROUND((c.act3*0.30),2),
                   ROUND(ROUND((c.act1*0.35),2)+ROUND((c.act2*0.35),2)+ROUND((c.act3*0.30),2),2) FROM calificacion c
                   INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                   INNER JOIN grado g  ON e.id_grado  = g.id_grado
                   INNER JOIN materia m ON c.id_materia = m.id_materia
                   WHERE c.no_periodo ='{periodo}' AND g.id_grado = {idGrado} AND m.materia = '{materia}' """
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listarNotasTipoLibreta(self, idEstudiante):
        conn = self.get_connection()
        sql = f"""
                    SELECT m.materia   
                    ,(CASE WHEN c.no_periodo  = 'I' THEN  (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='I' AND ms.materia= m.materia) END) AS TrimestreI
                    ,(CASE WHEN c.no_periodo  = 'I' THEN  (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='II' AND ms.materia= m.materia) END) AS 'Trimestre II'
                    ,(CASE WHEN c.no_periodo  = 'I' THEN  (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='III' AND ms.materia= m.materia) END) AS 'Trimestre III'
                    ,(CASE WHEN c.no_periodo  = 'I' THEN  (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='IIII' AND ms.materia= m.materia) END) AS 'Trimestre IV',

                    (ROUND(((SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='I' AND ms.materia= m.materia)+
                    (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='II' AND ms.materia= m.materia)+
                    (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='II' AND ms.materia= m.materia)+
                    (SELECT ROUND(ROUND((cp1.act1*0.35),2) + ROUND((cp1.act2*0.35),2) + ROUND((cp1.act3*0.30),2),2)  FROM calificacion cp1
                    INNER JOIN materia ms  on cp1.id_materia = ms.id_materia 
                    INNER JOIN estudiante e on cp1.id_estudiante = e.id_estudiante 
                    WHERE cp1.id_estudiante = 82  AND cp1.no_periodo ='IIII' AND ms.materia= m.materia))/4,2)) as 'inal'

                    FROM calificacion c
                    INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante
                    INNER JOIN grado g  ON e.id_grado  = g.id_grado
                    INNER JOIN materia m ON c.id_materia = m.id_materia
                    WHERE e.id_estudiante =82
                    GROUP BY m.materia;"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notas tipo LIBRETA "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()


    def getNotaFinalEstudianteX(self):
        conn = self.get_connection()
        sql = "SELECT * FROM nota"
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

                
    def listarNotasXEstudiantePerMat(self,idPeriodo,idMateria):
        conn = self.get_connection()
        sql = f"""SELECT c.act1,ROUND((c.act1*0.35),2), c.act2,ROUND((c.act2*0.35),2),c.act3,ROUND((c.act3*0.30),2) FROM calificacion c
                  INNER JOIN estudiante e ON c.id_estudiante =e.id_estudiante
                  INNER JOIN materia m ON c.id_materia = m.id_materia 
                WHERE e.id_estudiante ='{idPeriodo}' AND m.id_materia = '{idMateria}' """
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def listar_calificaciones_segun_idGrado_periodo_materia_bachillerato(self,idGrado,periodo,materia):
        conn = self.get_connection()
        sql = f"""SELECT c.id_calificacion,e.id_estudiante, e.nombre ,c.act1,c.act2,c.act3,c.act4 FROM calificacion c
                   INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante 
                   INNER JOIN grado g  ON e.id_grado  = g.id_grado
                   INNER JOIN materia m ON c.id_materia = m.id_materia
                   WHERE c.no_periodo ='{periodo}' AND g.id_grado = {idGrado} AND m.materia = '{materia}'"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def listar_notas(self):
        conn = self.get_connection()
        sql = "SELECT * FROM nota"

        try:
            cursor = conn.cursor()
            cursor.execute(self)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()


    def buscar_estudiante_calificando(self,idGrado,periodo,materia,estudiante):
        conn = self.get_connection()
        sql = f"""SELECT c.id_calificacion,e.id_estudiante, e.nombre ,c.act1,c.act2,c.act3,c.act4 FROM calificacion c
                   INNER JOIN estudiante e ON c.id_estudiante = e.id_estudiante 
                   INNER JOIN grado g  ON e.id_grado  = g.id_grado
                   INNER JOIN materia m ON c.id_materia = m.id_materia
                   WHERE c.no_periodo ='{periodo}' AND g.id_grado = {idGrado} AND m.materia = '{materia}' AND e.nombre LIKE '%{estudiante}%' """
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def listar_notas_nombre_asc_byIdGrado(self,id):
        conn = self.get_connection()
        sql = f"SELECT * FROM nota WHERE id_grado={id} ORDER BY nombre ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def listar_notas_nombre_nie_asc_byIdGrado(self,id):
        conn = self.get_connection()
        sql = f"SELECT * FROM nota WHERE id_grado={id} ORDER BY nie ASC"

        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR LISTAR notaS "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    def buscarnota(self,nota,idGrado):
        conn = self.get_connection()
        sql = f"SELECT * FROM nota WHERE id_grado = {idGrado} AND nombre LIKE '%{nota}%' OR nie  LIKE '%{nota}%' "
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            notas = cursor.fetchall()
            return notas
        except Error as e:
            print("ERROR busqueda notas "+str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()