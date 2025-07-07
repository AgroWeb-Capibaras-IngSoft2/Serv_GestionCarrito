from Application.RepositoriesI.CarritoInterfaces import UtilsI
import psycopg2
class UtilsAdapter(UtilsI):
    def __init__(self):
        try:
            self.connection=psycopg2.connect("psql 'postgresql://neondb_owner:npg_iHtshJ2kBE4o@ep-proud-dust-a8y6xl7k-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'")
        except Exception as e:
            raise ValueError(str(e))
        
    def validarExistenciaCarrito(self, numberDocument, typeDocument):
        sqlQuery="""SELECT id_carrito
                    FROM carrito
                    WHERE userdocument=%s AND typeDocument=%s ;"""
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
                WHERE numberDocument=%s AND typeDocument=%s;
        """
        result=None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery)
                result=cursor.fetchone()
        except Exception as e:
            raise ValueError(str(e))
        self.connection.close()
        return result[0]