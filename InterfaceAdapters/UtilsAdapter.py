from Application.RepositoriesI.CarritoInterfaces import UtilsI
import psycopg2
class UtilsAdapter(UtilsI):
    def __init__(self,conexion):
        try:
            self.connection=conexion
        except Exception as e:
            raise ValueError(str(e))
        
    def validarExistenciaCarrito(self, numberDocument, typeDocument):
        sqlQuery="""SELECT id_carrito
                    FROM carrito
                    WHERE userdocument=%s AND userdocumenttype=%s ;"""
        rows=None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(numberDocument,typeDocument))
                rows=cursor.fetchall()
                if(len(rows)!=0):
                    return True
                else:
                    return False
        except Exception as e:
            raise ValueError(str(e))
        self.connection.close()
        return False


    def obtenerIdCarrito(self, numberDocument, typeDocument):
        sqlQuery="""
                SELECT id_carrito 
                FROM carrito
                WHERE userdocument=%s AND userdocumenttype=%s;
        """
        result=None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(numberDocument,typeDocument))
                result=cursor.fetchone()
        except Exception as e:
            raise ValueError(str(e))
        return result