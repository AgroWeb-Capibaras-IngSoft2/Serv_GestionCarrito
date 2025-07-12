from Application.RepositoriesI.CarritoInterfaces import CambiarCantidadProdI
from Domain.ItemCarrito import ItemCarrito
import psycopg2
class CambiarCantidadAdapter(CambiarCantidadProdI):
    def __init__(self,conexion):
        self.conexion=conexion

    def cambiarCantidad(self, itemCarrito:ItemCarrito):
        try:
            with self.conexion.cursor() as cursor:
                sqlQuery="""
                            UPDATE item_carrito SET cantidad=%s
                            WHERE id_carrito=%s AND product_id=%s;
                        """
                cursor.execute(sqlQuery,(itemCarrito.cantidad,
                                         itemCarrito.id_carrito,
                                         itemCarrito.product_id))
                self.conexion.commit()
                return {"Success":True,"message":"Item Actualizado"}
        except psycopg2.Error as e:
            self.conexion.rollback()
            print("ENTRO ACÁ")
            return {"Success":False,"message":str(e)}
