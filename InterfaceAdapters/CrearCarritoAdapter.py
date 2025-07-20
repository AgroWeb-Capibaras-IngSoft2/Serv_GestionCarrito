from Application.RepositoriesI.CarritoInterfaces import CrearCarrritoI
from Domain.Carrito import Carrito
import psycopg2

class CrearCarritoAdapter(CrearCarrritoI):
    def __init__(self, pool):
        self.pool = pool

    def crearCarrito(self, newCarrito: Carrito):
        connection = self.pool.getconn()
        try:
            with connection.cursor() as cursor:
                sqlQuery = """
                    INSERT INTO carrito (userdocument, userdocumenttype)
                    VALUES (%s, %s);
                """
                cursor.execute(sqlQuery, (newCarrito.user_document, newCarrito.user_documentType))
            connection.commit()
            return {"Success": True, "message": "Carrito Creado"}
        except Exception as e:
            connection.rollback()
            return {"Success": False, "error": str(e)}
        finally:
            self.pool.putconn(connection)