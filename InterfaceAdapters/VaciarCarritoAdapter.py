import psycopg2
from Application.RepositoriesI.CarritoInterfaces import VaciarCarritoI
class VaciarCarritoAdapter(VaciarCarritoI):
    def __init__(self,pool):
        try:
            self.pool=pool
        except Exception as e:
            raise ValueError(str(e))

    def vaciarCarrito(self, id_carrito):
        connection = self.pool.getconn()
        try:
            with connection.cursor() as cursor:
                sqlQuery="""
                            DELETE FROM item_carrito
                            WHERE id_carrito = %s ;
                """
                cursor.execute(sqlQuery,(id_carrito,))  # Agregué la coma que faltaba
                afectadas = cursor.rowcount
                connection.commit()
            if(afectadas!=0):
                return {"Success":True,"message":"Carrito vaciado con exito"}
            else:
                return {"Success":False,"message":"El carrito ya esta vaciado"}
        except psycopg2.Error as e:
            connection.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            connection.rollback()  # Agregué rollback que faltaba
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(connection)