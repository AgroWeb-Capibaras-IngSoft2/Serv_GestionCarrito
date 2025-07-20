from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import CrearCarrritoI
from Application.RepositoriesI.CarritoInterfaces import UtilsI
from Domain.Carrito import Carrito
@dataclass
class CrearCarritoUseCase:
    '''El caso de uso depende de una abstracción no de una
     implementacion concreta'''
    crearCarrRepo:CrearCarrritoI
    utils:UtilsI


    def crearCarrito(self,usrDocument:str,userDocType:str):
        if(not(self.utils.validarExistenciaCarrito(usrDocument,userDocType))): #Si el carrito no existe se crea uno
            try:
                new_carrito = Carrito(user_document=usrDocument,user_documentType=userDocType)
                self.crearCarrRepo.crearCarrito(new_carrito)
                return {"Success":True,"message":"Carrito creado con exito","id_carrito":new_carrito.carrito_id}

            except Exception as e:
                raise ValueError(str(e))
        else:
            id=self.utils.obtenerIdCarrito(usrDocument,userDocType)[0]
            print(id,type(id))
            return{"Success":False,"message":"El carrito ya existe","id_carrito":id}



