from abc import ABC, abstractmethod
from Domain.Carrito import Carrito
from Domain.ItemCarrito import ItemCarrito
class CrearCarrritoI (ABC):
    @abstractmethod
    def crearCarrito(self,newCarrito:Carrito)->dict:
        pass

class VaciarCarritoI (ABC):
    @abstractmethod
    def vaciarCarrito(self,id_carrito:int):
        pass

class AnadirProdCarritoI(ABC):
    @abstractmethod
    def anadirProducto(self,newProd:ItemCarrito):
        pass

class EliminarProdCarritoI(ABC):
    @abstractmethod
    def eliminarProd(self,id_carrito:str,productId:str):
        pass

class CambiarCantidadProdI(ABC):
    @abstractmethod
    def cambiarCantidad(self,newItem:ItemCarrito):
        pass

class ObtenerCarritoI(ABC):
    @abstractmethod
    def getCarritoItems(self,id_carrito):
        pass
    @abstractmethod
    def getCarritoInfo(self,id_carrito):
        pass

class UtilsI(ABC):
    @abstractmethod
    def validarExistenciaCarrito(self,numberDocument:str,typeDocument:str)->bool:
        pass
    @abstractmethod
    def obtenerIdCarrito(self,numberDocument:str,typeDocument:str)->int:
        pass
    @abstractmethod
    def obtainItem(self,id_carrito:int,id_product:str)->dict:
        pass

    @abstractmethod
    def verificarExistenciaProd(self,id_carrito:int,id_product:str):
        pass

    @abstractmethod
    def existsCarrito(self,id_carrito:int):
        pass

    @abstractmethod
    def getUserData(self,id_carrito):
        pass



