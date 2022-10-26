import sqlite3
from sqlite3 import Error

class Conexion:
    def __init__(self) -> None:
        self._basedatos = 'db/school.db'
        self._conex = None
    
    @property
    def conex(self):
        return self._conex
    @conex.setter
    def conex(self,conex):
        self._conex = conex

    def get_connection(self):
        try:
            conn = sqlite3.connect(self._basedatos)
            self._conex=conn
            cur= self._conex.cursor()
            # cur.execute("CREATE TABLE grado (id_grado INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,grado TEXT NOT NULL,seccion TEXT NOT NULL)")
            # print("CONEXION ESTABLECIDA")
            return self._conex
        except Error as e:
            print('ERROR: '+str(e))
    
    def close_conexion(self):
        self._conex.close()

    

