from Application.RepositoriesI.CarritoInterfaces import EliminarProdCarritoI
import psycopg2
class EliminarProductoAdapter(EliminarProdCarritoI):
    def __init__(self,conexion):
        self.conexion=conexion

    def eliminarProd(self, id_carrito, productId):
        try:
            with self.conexion.cursor() as cursor:
                sqlQuery="""DELETE FROM item_carrito
                            WHERE id_carrito=%s AND product_id=%s ;"""
                cursor.execute(sqlQuery,(id_carrito,productId))
                self.conexion.commit()
                return {"Success":True,"message":"Producto eliminado del carrito"}
        except psycopg2.Error as e:
            self.conexion.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            self.conexion.rollback()
            return {"Success":False,"message":str(e)}

