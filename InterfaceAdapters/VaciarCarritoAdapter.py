import psycopg2
from Application.RepositoriesI.CarritoInterfaces import VaciarCarritoI
from InterfaceAdapters.UtilsAdapter import UtilsAdapter
class VaciarCarritoAdapter(VaciarCarritoI):
    def __init__(self):
        try:
            self.connection=psycopg2.connect("psql 'postgresql://neondb_owner:npg_iHtshJ2kBE4o@ep-proud-dust-a8y6xl7k-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require'")
        except Exception as e:
            raise ValueError(str(e))
        
    def vaciarCarrito(self, numberDocument, typeDocuemt):
        util=UtilsAdapter()
        if(util.validarExistenciaCarrito()):
            id_carrito=util.obtenerIdCarrito()
            try:
                with self.connection.cursor() as cursor:
                    sqlQuery="""
                            DELETE FROM item_carrito
                            WHERE id_carrito = %s ;
                    """
                    cursor.execute(sqlQuery,(id_carrito))
            except Exception as e:
                self.connection.rollback()
                raise ValueError (str(e))
            self.connection.commit()
            self.connection.close()
            return {"Success":True,"message":"Carrito vaciado con exito"}
            
        else:
            return {"Success":False,"message":"Este usuario no tiene un carrito creado"}