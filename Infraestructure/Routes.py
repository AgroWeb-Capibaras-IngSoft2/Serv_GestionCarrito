from flask import Blueprint,request,jsonify
from Application.UseCases.CrearCarritoUseCase import CrearCarritoUseCase
from Application.UseCases.AnadirProdUseCase import AnadirProductoUseCase
from InterfaceAdapters.CrearCarritoAdapter import CrearCarritoAdapter
from InterfaceAdapters.UtilsAdapter import UtilsAdapter
from InterfaceAdapters.AnadirProdAdapter import AnadirProdAdapter
from Infraestructure.DB import DB
from Infraestructure.CommunicationProdService import CommunicationProdService
from Infraestructure.testProdInfo import chooseProduct


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
#Creamos adaptador de anadirProd
addProdAdapter=AnadirProdAdapter(conexion)
#Caso de Uso anadir Producto
anadirProdUseCase=AnadirProductoUseCase(addProdAdapter,utils)



#Un carrito se crea cuando se crea un usuario
@bp.route("/carrito/create",methods=["POST"])
def crear_carrito():
    data=request.get_json()
    #Esta data se pasa al caso de uso encargado
    resul=createCarUseCase.crearCarrito(data.get("userDocument"),data.get("docType"))
    #TODO: Cerrar conexión
    if(resul["Success"]):
        return jsonify(resul),200
    else:
        return jsonify(resul),409

#Añadir un nuevo producto al carrito
@bp.route("/carrito/addProduct",methods=["POST"])
def add_product():
        #prodService=CommunicationProdService()
        #prodInfo=prodService.obtainProductInfo()
        userDoc="1234567"
        doctyType="CC"
        medida="LB"
        cantidad=3
        prod=chooseProduct()
        prod["cantidad"]=cantidad
        prod["medida"]=medida

        resul=anadirProdUseCase.addProdCarrito(userDoc,doctyType,prod)
        if(resul["Success"]):
            return jsonify({"Success":True,"message":resul["message"]}),201
        else:
            return jsonify({"Success":False,"message":resul["message"]}),500


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

@bp.route("/carrito/getCarritoId",methods=["GET"])
def getCarritoId():
    data=request.get_json()
    id=anadirProdUseCase.addProdCarrito(data.get("userdocument"),data.get("userdoctype"))
    if(not id==None):
        return({"Success":True,"Id carrito":id})
    else:
        return({"Success":False,"Id carrito":"No existe"})





