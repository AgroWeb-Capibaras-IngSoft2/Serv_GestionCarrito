from Application.RepositoriesI.CarritoInterfaces import EliminarProdCarritoI
import psycopg2
class EliminarProductoAdapter(EliminarProdCarritoI):
    def __init__(self,pool):
        self.pool=pool

    def eliminarProd(self, id_carrito, productId):
        connection = self.pool.getconn()
        try:
            with connection.cursor() as cursor:
                sqlQuery="""DELETE FROM item_carrito
                            WHERE id_carrito=%s AND product_id=%s ;"""
                cursor.execute(sqlQuery,(id_carrito,productId))
                connection.commit()
                return {"Success":True,"message":"Producto eliminado del carrito"}
        except psycopg2.Error as e:
            connection.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            connection.rollback()
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(connection)

