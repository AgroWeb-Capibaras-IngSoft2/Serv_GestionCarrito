from Application.RepositoriesI.CarritoInterfaces import UtilsI
import psycopg2
from psycopg2.extras import RealDictCursor
class UtilsAdapter(UtilsI):
    def __init__(self,pool):
        try:
            self.pool=pool
        except Exception as e:
            raise ValueError(str(e))
        
    def validarExistenciaCarrito(self, numberDocument, typeDocument):
        # Rollback preventivo para limpiar cualquier transacción pendiente
        self.connection=self.pool.getconn()
        try:
            self.connection.rollback()
        except:
            pass
            
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
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            raise ValueError(str(e))
        finally:
            self.pool.putconn(self.connection)


    def existsCarrito(self,id_carrito:int):
        # Rollback preventivo para limpiar cualquier transacción pendiente
        self.connection=self.pool.getconn()
        try:
            self.connection.rollback()
        except:
            pass
            
        try:
            sqlQuery="""
                SELECT id_carrito
                FROM carrito WHERE id_carrito=%s ;
            """
            with self.connection.cursor() as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                result=cursor.fetchone()
                if(result):
                    return {"Success":True,"result":result}
                else:
                    return{"Success":False,"message":"No se encontro un carrito con este id"}
        except psycopg2.Error as e:
            # Hacer rollback en caso de error de DB
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            # Hacer rollback en caso de cualquier error
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(self.connection)


    def obtenerIdCarrito(self, numberDocument, typeDocument):
        # Rollback preventivo para limpiar cualquier transacción pendiente
        self.connection=self.pool.getconn()
        try:
            self.connection.rollback()
        except:
            pass
            
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
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            raise ValueError(str(e))
        finally:
            self.pool.putconn(self.connection)
        return result

    def obtainItem(self,id_carrito,id_product):
        self.connection=self.pool.getconn()
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
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(self.connection)

    def verificarExistenciaProd(self, id_carrito, id_product):
        print("id carrito",id_carrito)
        print("id product",id_product)
        self.connection=self.pool.getconn()
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
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        except Exception as e:
            print("ERROR EXC 2")
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            return {"Success":False,"message":str(e)}
        finally:
            self.pool.putconn(self.connection)
    
    def getUserData(self, id_carrito):
        self.connection=self.pool.getconn()
        sqlQuery="""SELECT userdocument,userdocumenttype
                    FROM carrito where id_carrito=%s ;"""
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(sqlQuery,(id_carrito,))
                resul=cursor.fetchone()
                return ({"Success":True,"resul":resul})
        except Exception as e:
            print("ERROR ACA")
            # Hacer rollback para limpiar la transacción
            self.connection.rollback()
            raise ValueError(str(e))
        finally:
            self.pool.putconn(self.conexion)