from Application.RepositoriesI.CarritoInterfaces import AnadirProdCarritoI
from Domain.ItemCarrito import ItemCarrito
class AnadirProdAdapter(AnadirProdCarritoI):
    def __init__(self,conexion):
        self.conexion=conexion

    def anadirProducto(self,newProd:ItemCarrito):
        try:
            with self.conexion.cursor() as cursor:
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
        except Exception as e:
            raise ValueError(str(e))
