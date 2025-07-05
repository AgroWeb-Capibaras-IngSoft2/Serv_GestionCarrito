from dataclasses import dataclass
from datetime import date
@dataclass
class Carrito:
    carrito_id:int
    user_document:str
    user_documentType:str
    creationDate:date
    total:float=0.00

    #TODO: Añadir cedula de extranjería
    def validar_tipo_doc(self):
        return self.user_documentType in ["CC","TI"]

    def __post_init__(self):
       if (not self.validar_tipo_doc):
            raise ValueError("El tipo de documento no es valido")

