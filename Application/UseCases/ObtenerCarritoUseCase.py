from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import ObtenerCarritoI,UtilsI
@dataclass
class ObtenerCarritoUseCase:
    obtCarrI:ObtenerCarritoI
    utlis:UtilsI

    def getAllCarritoInfo(self,id_carrito):
        try:
            exists=self.utlis.existsCarrito(id_carrito)
            if(not exists):
                return {"Success":False,"message":"No existe"}
            respGeneral = self.obtCarrI.getCarritoInfo(id_carrito)
            respItems = self.obtCarrI.getCarritoItems(id_carrito)

            successGeneral = respGeneral["Success"]
            generalInfo = respGeneral["result"]

            successItems = respItems["Success"]
            items = respItems["result"]

            if(successGeneral and successItems):
                generalInfo["items"]=items
                generalInfo["total"]=self.calcularTotal(items)
                return {"Success":True,"resul":generalInfo}
        except Exception as e:
            return {"Success":False,"message":str(e)}
    
    def calcularTotal(self,items:dict):
        if(items):
            return sum(item["total_prod"] for item in items)
        return 0