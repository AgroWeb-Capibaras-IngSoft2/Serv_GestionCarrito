
import psycopg2
from psycopg2.extras import RealDictCursor
from Application.RepositoriesI.CarritoInterfaces import ObtenerCarritoI
class ObtenerCarritoAdapter(ObtenerCarritoI):
    def __init__(self,conexion):
        self.conexion=conexion

    def getCarritoInfo(self,id_carrito):
        sqlQuery="""
                SELECT id_carrito,total
                FROM carrito
                WHERE id_carrito=%s ;
                """
        try:
            with self.conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                resul= cursor.fetchone()
                return {"Success":True,"result":resul}
        except psycopg2.Error as e:
            return({"Success":False,"message":str(e)})
        except Exception as e:
            return({"Success":False,"message":str(e)})


    def getCarritoItems(self,id_carrito):
        sqlQuery="""
                SELECT product_id,product_name,cantidad,medida,total_prod
                FROM item_carrito
                WHERE id_carrito=%s ;
                """
        try:
            with self.conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                resul= cursor.fetchall()
                return {"Success":True,"result":resul}
        except psycopg2.Error as e:
            return({"Success":False,"message":str(e)})
        except Exception as e:
            return({"Success":False,"message":str(e)})