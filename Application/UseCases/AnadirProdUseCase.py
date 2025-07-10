from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import AnadirProdCarritoI,UtilsI
from Domain.ItemCarrito import ItemCarrito

@dataclass
class AnadirProductoUseCase:
    addProdI:AnadirProdCarritoI
    utils:UtilsI

    def addProdCarrito(self,userDocument,documentType,prodInfo:dict):
        id_carrito=self.utils.obtenerIdCarrito(userDocument,documentType)
        try:
            itemCar=ItemCarrito(
                id_carrito,
                userDocument=userDocument,
                userDocumentType=documentType,
                product_id=prodInfo["product_id"],
                product_name=prodInfo["prod_name"],
                cantidad=prodInfo["cantidad"],
                medida=prodInfo["medida"]
            )
            itemCar.calcularTotal(prodInfo["price"])
            return self.addProdI.anadirProducto(itemCar)
        except Exception as e:
            return {"Success":False,"message":str(e)}




