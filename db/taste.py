import sqlite3
from sqlite3 import Error
from Conexion import *

if __name__=='__main__':
    con = Conexion()
    con.get_connection()