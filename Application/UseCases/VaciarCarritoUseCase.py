from dataclasses import dataclass
from Application.RepositoriesI.CarritoInterfaces import VaciarCarritoI,UtilsI
@dataclass
class VaciarCarritoUseCase:
    vaciarCarrI: VaciarCarritoI
    utils:UtilsI

    def vaciarCarritoUC(self,id_carrito):
        resul=self.utils.existsCarrito(id_carrito)["Success"]
        if(resul):
            try:
                return self.vaciarCarrI.vaciarCarrito(id_carrito)
            except Exception as e:
                return {"Success":False,"message":str(e)}
        return {"Success":False,"message":"No existe el carrito"}