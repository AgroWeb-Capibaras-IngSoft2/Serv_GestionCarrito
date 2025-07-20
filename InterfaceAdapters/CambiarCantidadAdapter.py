from Application.RepositoriesI.CarritoInterfaces import CambiarCantidadProdI
from Domain.ItemCarrito import ItemCarrito
import psycopg2
class CambiarCantidadAdapter(CambiarCantidadProdI):
    def __init__(self,pool):
        self.pool=pool

    def cambiarCantidad(self, itemCarrito:ItemCarrito):
        connection = self.pool.getconn()
        try:
            with connection.cursor() as cursor:
                sqlQuery="""
                            UPDATE item_carrito SET cantidad=%s,total_prod=%s
                            WHERE id_carrito=%s AND product_id=%s;
                        """
                cursor.execute(sqlQuery,(itemCarrito.cantidad,
                                         itemCarrito.total_prod,
                                         itemCarrito.id_carrito,
                                         itemCarrito.product_id))
                connection.commit()
                return {"Success":True,"message":"Item Actualizado"}
        except psycopg2.Error as e:
            connection.rollback()
            print("ENTRO ACÁ")
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(connection)
