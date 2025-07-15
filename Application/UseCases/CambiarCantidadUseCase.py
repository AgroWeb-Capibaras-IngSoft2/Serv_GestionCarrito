from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import CambiarCantidadProdI
from Application.RepositoriesI.CarritoInterfaces import UtilsI
from Domain.ItemCarrito import ItemCarrito
@dataclass
class CambiarCantidadUseCase:
    cambiarProdI:CambiarCantidadProdI
    utils:UtilsI

    def cambiarCantidad(self,prodInfo:dict,newCantidad,id_carrito,id_prod):
        try:
            #Traemos la información actual del item, con el precio y cantidad antigua
            currentItemSucc=self.utils.obtainItem(id_carrito,id_prod)
            if(not currentItemSucc["Success"]):
                return {"Success":False,"message":currentItemSucc["message"]}
            currentItem=currentItemSucc["resul"]
            if(currentItem==None):
                return {"Success":False,"message":"No se encontro un item actual para cambiar la cantidad del producto"}
            #Creamos un nuevo item con la info actualizada (cantidad y precio)
            print(currentItem)
            updateItem= ItemCarrito(
                id_carrito=currentItem["id_carrito"],
                userDocument=currentItem["userdocument"],
                userDocumentType=currentItem["userdocumenttype"],
                product_id=currentItem["product_id"],
                product_name=currentItem["product_name"],
                cantidad=newCantidad,
                medida=currentItem["medida"]
            )
            updateItem.calcularTotal(prodInfo["price"])
            return self.cambiarProdI.cambiarCantidad(updateItem)
        except Exception as e:
            print(str(e))
            raise ValueError(str(e))
            print("ERROR USE CASE")
            return {"Success":False,"message":str(e)}


