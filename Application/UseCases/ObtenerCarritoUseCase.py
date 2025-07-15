from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import ObtenerCarritoI,UtilsI
@dataclass
class ObtenerCarritoUseCase:
    obtCarrI:ObtenerCarritoI
    utlis:UtilsI

    def getAllCarritoInfo(self,id_carrito):
        try:
            respGeneral = self.obtCarrI.getCarritoInfo(id_carrito)
            respItems = self.obtCarrI.getCarritoItems(id_carrito)

            successGeneral = respGeneral["Success"]
            generalInfo = respGeneral["result"]

            successItems = respItems["Success"]
            items = respItems["result"]

            if(successGeneral and successItems):
                generalInfo["items"]=items
                return {"Success":True,"resul":generalInfo}
        except Exception as e:
            return {"Success":False,"message":str(e)}