from Application.RepositoriesI.CarritoInterfaces import CrearCarrritoI
from Domain.Carrito import Carrito
import psycopg2
class CrearCarritoAdapter(CrearCarrritoI):
    def __init__(self,conexion):
        #Pasamos una conexion
        self.connection=conexion

    def crearCarrito(self, newCarrito:Carrito):
        try:
            with self.connection.cursor() as cursor:
                sqlQuery="""
                    INSERT INTO carrito (userdocument,userdocumenttype)
                    VALUES (%s,%s);
                """
                cursor.execute(sqlQuery,(newCarrito.user_document,newCarrito.user_documentType))
            self.connection.commit()
            return {"Success": True,"message":"Carrito Creado"}
        except Exception as e:
            self.connection.rollback()
            return {"Success":False,"error":str(e)}