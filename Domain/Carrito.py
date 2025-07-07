from dataclasses import dataclass
from datetime import date
@dataclass
class Carrito:
    user_document:str
    user_documentType:str
    total:float=0.00
    carrito_id=0
    creationDate=date.today()


    #TODO: Añadir cedula de extranjería
    def validar_tipo_doc(self):
        return self.user_documentType in ["CC","TI"]

    def __post_init__(self):
       if (not self.validar_tipo_doc):
            raise ValueError("El tipo de documento no es valido")

