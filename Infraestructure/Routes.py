from flask import Blueprint,request,jsonify
from Application.UseCases.CrearCarritoUseCase import CrearCarritoUseCase
from InterfaceAdapters.CrearCarritoAdapter import CrearCarritoAdapter
from InterfaceAdapters.UtilsAdapter import UtilsAdapter
from Infraestructure.DB import DB

bp=Blueprint("carrito",__name__)
#Creamos una instancia de DB
db=DB()
db.crearPool()
conexion=db.obtenerConexion()
#Creamos un adaptador de crear carrito
crearCarAdapter=CrearCarritoAdapter(conexion)
#Creamos un adaptador de utils
utils= UtilsAdapter(conexion)
#Caso de Uso Crear Carrito
createCarUseCase=CrearCarritoUseCase(crearCarAdapter,utils)

#Un carrito se crea cuando se crea un usuario
@bp.route("/carrito/create",methods=["POST"])
def crear_carrito():
    data=request.get_json()
    #Esta data se pasa al caso de uso encargado
    resul=createCarUseCase.crearCarrito(data.get("userDocument"),data.get("docType"))
    #TODO: Cerrar conexión
    return jsonify(resul),200

#Añadir un nuevo producto al carrito
@bp.route("/carrito/addProduct",methods=["POST"])
def add_product():    
    data=request.get_json()
    pass
#Cambiar la cantidad de un producto
@bp.route("/carrito/changeQuantity",methods=["PUT"])
def cambiar_cantidad():
    data=request.get_json()
    pass
#Eliminar producto del carrito
@bp.route("/carrito/deleteProduct",methods=["DELETE"])
def delete_product():
    data=request.get_json()
    pass
#Vaciar carrito
@bp.route("/carrito/vaciar",methods=["DELETE"])
def vaciar_carrito():
    data=request.get_json()
    pass

#Obtener carrito
@bp.route("/carrito/getCarrito",methods=["GET"])
def get_carrito():
    data=request.get_json()
    pass


