from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import EliminarProdCarritoI,UtilsI
@dataclass
class EliminarProductoUseCase:
    eliminarProd:EliminarProdCarritoI
    utils:UtilsI

    def elimiarProdCarrito(self,product_id,id_carrito):
        try:
            resul=self.utils.verificarExistenciaProd(id_carrito,product_id)["result"]
            if(resul==None):
                return {"Success":False,"message":"El producto no existe en el carrito"}
            resul=self.eliminarProd.eliminarProd(id_carrito,product_id)
            return {"Success":True,"message":resul["message"]}
        except Exception as e:
            return {"Success":False,"message":str(e)}