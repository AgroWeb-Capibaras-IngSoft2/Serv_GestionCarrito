from flask import Blueprint,request,jsonify
from Application.UseCases.CrearCarritoUseCase import CrearCarritoUseCase
bp=Blueprint("carrito",__name__)

#Caso de Uso Crear Carrito
createCarUseCase=CrearCarritoUseCase()

#Un carrito se crea cuando se crea un usuario
@bp.route("carrito/create",methods=["POST"])
def crear_carrito():
    data=request.get_json()
    #Esta data se pasa al caso de uso encargado
    createCarUseCase.crearCarrito(data.get("userDocument"),data.get("docType"))
    pass
#Añadir un nuevo producto al carrito
@bp.route("carrito/addProduct",methods=["POST"])
def add_product():    
    data=request.get_json()
    pass
#Cambiar la cantidad de un producto
@bp.route("carrito/changeQuantity",methods=["PUT"])
def cambiar_cantidad():
    data=request.get_json()
    pass
#Eliminar producto del carrito
@bp.route("carrito/deleteProduct",methods=["DELETE"])
def delete_product():
    data=request.get_json()
    pass
#Vaciar carrito
@bp.route("carrito/vaciar",methods=["DELETE"])
def vaciar_carrito():
    data=request.get_json()
    pass

#Obtener carrito
@bp.route("carrito/getCarrito",methods=["GET"])
def get_carrito():
    data=request.get_json()
    pass


