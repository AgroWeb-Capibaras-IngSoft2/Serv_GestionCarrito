from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import AnadirProdCarritoI,UtilsI
from Domain.ItemCarrito import ItemCarrito

@dataclass
class AnadirProductoUseCase:
    addProdI:AnadirProdCarritoI
    utils:UtilsI

    def addProdCarrito(self,id_carrito,prodInfo:dict):
        try:
            userData=self.utils.getUserData(id_carrito)["resul"]
            print(userData)
            itemCar=ItemCarrito(
                id_carrito,
                userDocument=userData["userdocument"],
                userDocumentType=userData["userdocumenttype"],
                product_id=prodInfo["productId"],
                product_name=prodInfo["name"],
                cantidad=prodInfo["cantidad"],
                medida=prodInfo["unit"]
            )
            itemCar.calcularTotal(prodInfo["price"])
            return self.addProdI.anadirProducto(itemCar)
        except Exception as e:
            return {"Success":False,"message":str(e)}




