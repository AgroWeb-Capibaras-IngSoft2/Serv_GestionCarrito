from Application.RepositoriesI.CarritoInterfaces import UtilsI
import psycopg2
from psycopg2.extras import RealDictCursor
class UtilsAdapter(UtilsI):
    def __init__(self,conexion):
        try:
            self.connection=conexion
        except Exception as e:
            raise ValueError(str(e))
        
    def validarExistenciaCarrito(self, numberDocument, typeDocument):
        sqlQuery="""SELECT id_carrito
                    FROM carrito
                    WHERE userdocument=%s AND userdocumenttype=%s ;"""
        rows=None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(numberDocument,typeDocument))
                rows=cursor.fetchall()
                if(len(rows)!=0):
                    return True
                else:
                    return False
        except Exception as e:
            raise ValueError(str(e))
        self.connection.close()
        return False


    def obtenerIdCarrito(self, numberDocument, typeDocument):
        sqlQuery="""
                SELECT id_carrito
                FROM carrito
                WHERE userdocument=%s AND userdocumenttype=%s;
        """
        result=None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(numberDocument,typeDocument))
                result=cursor.fetchone()
        except Exception as e:
            raise ValueError(str(e))
        return result

    def obtainItem(self,id_carrito,id_product):
        sqlQuery="""
                SELECT iditem,id_carrito,userdocument,userdocumenttype,
                        product_id,product_name,cantidad,medida
                FROM item_carrito
                WHERE id_carrito=%s AND product_id=%s;
        """
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,
                                         id_product))
                result=cursor.fetchone()
                return {"Success":True,"resul":result}
        except psycopg2.Error as e:
            return {"Success":False,"message":str(e)}

    def verificarExistenciaProd(self, id_carrito, id_product):
        print("id carrito",id_carrito)
        print("id product",id_product)
        try:
            sqlQuery="""
                SELECT id_carrito,product_id
                FROM item_carrito WHERE id_carrito=%s AND product_id=%s ;
            """
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(id_carrito,id_product))
                result=cursor.fetchone()
                print("result:",result)
                return {"Success":True,"result":result}
        except psycopg2.Error as e:
            print("ERROR EXC 1")
            return {"Success":False,"message":str(e)}
        except Exception as e:
            print("ERROR EXC 2")
            return {"Success":False,"message":str(e)}