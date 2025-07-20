from dataclasses import dataclass
from datetime import date
@dataclass
class ItemCarrito:
    id_carrito:str
    userDocument:str
    userDocumentType:str
    product_id:str
    product_name:str
    cantidad:int
    medida:str
    total_prod:float=0
    idItem=0

    #TODO: Validar el tipo de medida de los productos

    def __post_init__(self):
        if(not self.validar_cantidad):
            raise ValueError("La cantidad de producto no es valida")
    def validar_cantidad(self):
        return self.cantidad>0

    def calcularTotal(self,precio):
        self.total_prod=self.cantidad*precio
