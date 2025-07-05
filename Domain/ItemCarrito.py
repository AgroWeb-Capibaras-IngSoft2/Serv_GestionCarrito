from dataclasses import dataclass
from datetime import date
@dataclass
class ItemCarrito:
    idItem:int
    id_carrito:int
    userDocument:str
    userDocumentType:str
    product_id:int
    product_name:str
    cantidad:int
    medida:str
    total_prod:float=0

    #TODO: Validar el tipo de medida de los productos
    #TODO: Calcular el precio total
    
    def __post_init__(self):
        if(not self.validar_cantidad):
            raise ValueError("La cantidad de producto no es valida")
    def validar_cantidad(self):
        return self.cantidad>0
