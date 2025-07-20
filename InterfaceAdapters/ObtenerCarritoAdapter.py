
import psycopg2
from psycopg2.extras import RealDictCursor
from Application.RepositoriesI.CarritoInterfaces import ObtenerCarritoI
class ObtenerCarritoAdapter(ObtenerCarritoI):
    def __init__(self,pool):
        self.pool=pool

    def getCarritoInfo(self,id_carrito):
        connection = self.pool.getconn()
        try:
            sqlQuery="""
                    SELECT id_carrito
                    FROM carrito
                    WHERE id_carrito=%s ;
                    """
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                resul= cursor.fetchone()
                return {"Success":True,"result":resul}
        except psycopg2.Error as e:
            connection.rollback()
            return({"Success":False,"message":str(e)})
        except Exception as e:
            connection.rollback()
            return({"Success":False,"message":str(e)})
        finally:
            self.pool.putconn(connection)

    def getCarritoItems(self,id_carrito):
        connection = self.pool.getconn()
        try:
            sqlQuery="""
                    SELECT product_id,product_name,cantidad,medida,total_prod
                    FROM item_carrito
                    WHERE id_carrito=%s ;
                    """
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                resul= cursor.fetchall()
                return {"Success":True,"result":resul}
        except psycopg2.Error as e:
            connection.rollback()
            return({"Success":False,"message":str(e)})
        except Exception as e:
            connection.rollback()
            return({"Success":False,"message":str(e)})
        finally:
            self.pool.putconn(connection)

