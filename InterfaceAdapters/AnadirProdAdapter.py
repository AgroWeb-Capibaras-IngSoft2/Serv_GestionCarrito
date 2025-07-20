from Application.RepositoriesI.CarritoInterfaces import AnadirProdCarritoI
from Domain.ItemCarrito import ItemCarrito
import psycopg2
class AnadirProdAdapter(AnadirProdCarritoI):
    def __init__(self,pool):
        self.pool=pool

    def anadirProducto(self,newProd:ItemCarrito):
        connection = self.pool.getconn()
        try:
            with connection.cursor() as cursor:
                sqlQuery="""
                        INSERT INTO item_carrito (id_carrito,userdocument,userdocumenttype,product_id,product_name,cantidad,medida,total_prod)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
                        """
                cursor.execute(sqlQuery,(newProd.id_carrito,
                                         newProd.userDocument,
                                         newProd.userDocumentType,
                                         newProd.product_id,
                                         newProd.product_name,
                                         newProd.cantidad,
                                         newProd.medida,
                                         newProd.total_prod))
                connection.commit()
                return {"Success":True,"message":"Producto añadido exitosamente"}
        except psycopg2.errors.UniqueViolation as e:
            connection.rollback()
            return {"Success":False,"message":"El producto ya esta en el carrito"}
        except Exception as e:
            connection.rollback()
            raise ValueError(str(e))
        finally:
            self.pool.putconn(connection)
