from Application.RepositoriesI.CarritoInterfaces import CrearCarrritoI
import psycopg2
class CrearCarritoAdapter(CrearCarrritoI):
    def __init__(self):
        #Realizamos la conexión a la base de datos
        #TODO: Hacer un pool de conexiones
        try:
            self.connection=psycopg2.connect("psql 'postgresql://neondb_owner:npg_iHtshJ2kBE4o@ep-proud-dust-a8y6xl7k-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'")
        except Exception as e:
            raise ValueError(str(e)) 

    def crearCarrito(self, numberDocument, typeDocument):
        try:
            with self.connection.cursor() as cursor:
                sqlQuery="""
                    INSERT INTO carrito (userdocument,userdocumenttype)
                    VALUES (%s,%s);
                """
                cursor.execute(sqlQuery,(numberDocument,typeDocument))
            self.connection.commit()
            return {"Success": True,"message":"Carrito Creado"}
        except Exception as e:
            self.connection.rollback()
            return {"Success":False,"error":str(e)}
        finally:
            self.connection.close()