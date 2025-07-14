import psycopg2
from Application.RepositoriesI.CarritoInterfaces import VaciarCarritoI
class VaciarCarritoAdapter(VaciarCarritoI):
    def __init__(self,conexion):
        try:
            self.connection=conexion
        except Exception as e:
            raise ValueError(str(e))

    def vaciarCarrito(self, id_carrito):
        try:
            with self.connection.cursor() as cursor:
                sqlQuery="""
                            DELETE FROM item_carrito
                            WHERE id_carrito = %s ;
                """
                cursor.execute(sqlQuery,(id_carrito))
                afectadas = cursor.rowcount
                self.connection.commit()
            if(afectadas!=0):
                return {"Success":True,"message":"Carrito vaciado con exito"}
            else:
                return {"Success":False,"message":"El carrito ya esta vaciado"}
        except psycopg2.Error as e:
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            return {"Success":False,"message":str(e)}