from dataclasses import dataclass,field
from datetime import date
import uuid
@dataclass
class Carrito:
    user_document: str
    user_documentType: str
    total: float = 0.00
    carrito_id: str = field(default_factory=lambda: f"CARR-{str(uuid.uuid4())[:8].upper()}")
    creationDate: date = field(default_factory=date.today)


    #TODO: Añadir cedula de extranjería
    def validar_tipo_doc(self):
        return self.user_documentType in ["CC","TI","C.C","T.I","Cedula Extranjera"]

    def __post_init__(self):
       if (not self.validar_tipo_doc()):
            raise ValueError("El tipo de documento no es valido")

