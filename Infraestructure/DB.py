import os
from psycopg2 import pool
from dotenv import load_dotenv
class DB:
    def __init__(self):
        self.pool=None
        load_dotenv()
    
    #Método para crear un pool de conexiones
    def crearPool(self):
        if (self.pool==None):
            try:
                stringCon=os.getenv('DATA_BASE_URL')
                print(stringCon)
                self.pool=pool.SimpleConnectionPool(
                    1,
                    5,
                    stringCon
                )
                return{"Success":True,"message":"Pool creado exitosamente"}
            except Exception as e:
                raise ValueError(str(e))
        
        else:
            return {"Success":False,"message":"Ya existe un pool creado"}
    
    def obtenerConexion(self):
        if (not (self.pool == None)):
            try:
                return self.pool.getconn()
            except Exception as e:
                raise ValueError(str(e))
        else:
            raise ValueError("No existe un pool de conexiones")
    
    def liberarConexion(self,conexion):
        self.pool.putconn(conexion)
    
    def getPool(self):
        """Retorna el pool de conexiones"""
        if self.pool is not None:
            return self.pool
        else:
            raise ValueError("No existe un pool de conexiones")
    
    def cerrarConexiones(self):
        self.pool.closeall()
    
    def getPool(self):
        return self.pool