from abc import ABC, abstractmethod
class CrearCarrritoI (ABC):
    @abstractmethod
    def crearCarrito(self,numberDocument:str,typeDocument:str):
        pass
    
class VaciarCarritoI (ABC):
    @abstractmethod
    def vaciarCarrito(self,numberDocument:str,typeDocuemt:str):
        pass

class AnadirProdCarritoI(ABC):
    @abstractmethod
    def anadirProducto(self,numberDocument:str,typeDocument:str,productId:str,
                       nombreProd:str,cantidad:int):
        pass

class EliminarProdCarritoI(ABC):
    @abstractmethod
    def eliminarProd(self,numberDocument:str,typeDocument:str,productId):
        pass

class CambiarCantidadProdI(ABC):
    @abstractmethod
    def cambiarCantidad(self,numberDocument:str,typeDocument:str,productId,cantidad):
        pass

class ObtenerCarritoI(ABC):
    @abstractmethod
    def obtenerCarrito(self,numberDocument:str,typeDocument:str):
        pass

class UtilsI(ABC):
    @abstractmethod
    def validarExistenciaCarrito(self,numberDocument:str,typeDocument:str)->bool:
        pass
    @abstractmethod
    def obtenerIdCarrito(self,numberDocument:str,typeDocument:str)->int:
        pass


