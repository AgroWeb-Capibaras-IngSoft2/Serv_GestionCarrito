from flask import Blueprint,request,jsonify
from Application.UseCases.CrearCarritoUseCase import CrearCarritoUseCase
from Application.UseCases.AnadirProdUseCase import AnadirProductoUseCase
from Application.UseCases.CambiarCantidadUseCase import CambiarCantidadUseCase
from Application.UseCases.EliminarProductoUseCase import EliminarProductoUseCase
from Application.UseCases.VaciarCarritoUseCase import VaciarCarritoUseCase
from Application.UseCases.ObtenerCarritoUseCase import ObtenerCarritoUseCase
from InterfaceAdapters.CrearCarritoAdapter import CrearCarritoAdapter
from InterfaceAdapters.UtilsAdapter import UtilsAdapter
from InterfaceAdapters.AnadirProdAdapter import AnadirProdAdapter
from InterfaceAdapters.CambiarCantidadAdapter import CambiarCantidadAdapter
from InterfaceAdapters.EliminarProductoAdapter import EliminarProductoAdapter
from InterfaceAdapters.VaciarCarritoAdapter import VaciarCarritoAdapter
from InterfaceAdapters.ObtenerCarritoAdapter import ObtenerCarritoAdapter
from Infraestructure.DB import DB
from Infraestructure.CommunicationProdService import CommunicationProdService
from Infraestructure.testProdInfo import chooseProduct,getProdInfo


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
#Creamos adaptador de cambiar cantidad de prod
cambCantAdap=CambiarCantidadAdapter(conexion)
#Creamos caso de uso de cambiar cantidad
cambCabtiUseCase=CambiarCantidadUseCase(cambCantAdap,utils)
#Creamos adaptador de eliminarProducto
elimProdAdapter=EliminarProductoAdapter(conexion)
#Creamos el caso de uso
elimProdUseCase=EliminarProductoUseCase(elimProdAdapter,utils)
#Creamos adaptador de vaciar carrito
vaciarCarrAdap=VaciarCarritoAdapter(conexion)
#Creamos el caso de uso de vaciar carrito
vaciarCarUseCase=VaciarCarritoUseCase(vaciarCarrAdap,utils)
#Creamos adaptador de ObtenerCarrito
obtCarritoAdap=ObtenerCarritoAdapter(conexion)
#Creamos caso de uso de ObtenerCarrito
obtCarritoUseC=ObtenerCarritoUseCase(obtCarritoAdap,utils)

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
    try:
        data=request.get_json()
        prod_id=data.get("product_id")
        prodService=CommunicationProdService()
        prodInfo=prodService.obtainProductInfo(prod_id)
        print(prodInfo)
        print(type(prodInfo))
        id_carrito=data.get("id_carrito")
        cantidad=data.get("cantidad")
        prodInfo["cantidad"]=cantidad


        resul=anadirProdUseCase.addProdCarrito(id_carrito,prodInfo)
        if(resul["Success"]):
            return jsonify({"Success":True,"message":resul["message"]}),201
        else:
            return jsonify({"Success":False,"message":resul["message"]}),500
    except Exception as e:
        return jsonify({"Success":False,"message":str(e)})


#Cambiar la cantidad de un producto
@bp.route("/carrito/changeQuantity",methods=["PUT"])
def cambiar_cantidad():
    data=request.get_json()
    id_carrito=data.get("id_carrito")
    id_prod=data.get("product_id")
    new_quantity=data.get("cantidad")
    print(id_carrito,id_prod,new_quantity)
    try:
        prod=getProdInfo(id_prod)
        resul=cambCabtiUseCase.cambiarCantidad(prod,new_quantity,id_carrito,id_prod)
        if(resul["Success"]):
            return jsonify(resul),201
        else:
            return jsonify(resul),400
    except Exception as e:
        return jsonify({"Success":False,"message":str(e)}),500


#Eliminar producto del carrito
@bp.route("/carrito/deleteProduct",methods=["DELETE"])
def delete_product():
    try:
        data=request.get_json()
        product_id=data.get("product_id")
        carrito_id=data.get("carrito_id")
        resul=elimProdUseCase.elimiarProdCarrito(product_id,carrito_id)
        if(resul["Success"]):
            return jsonify({"Success":True,"message":"Producto Eliminado del carrito"}),201
        else:
            return jsonify({"Success":False,"message":resul["message"]}),404
    except Exception as e:
        return jsonify({"Success":False,"message":str(e)})

#Vaciar carrito
@bp.route("/carrito/vaciar",methods=["DELETE"])
def vaciar_carrito():
    id_carrito=request.args.get("id_carrito")
    if (id_carrito):
        resul=vaciarCarUseCase.vaciarCarritoUC(id_carrito)
        if(resul["Success"]):
            return jsonify(resul),200
        else:
            return jsonify(resul),500
    else:
        return jsonify({"Success":False,"message":"No se ha enviado un id de carrito para procesar la solicitud"}),400


#Obtener carrito
@bp.route("/carrito/getCarrito/<id>",methods=["GET"])
def get_carrito(id):
    try:
        result=obtCarritoUseC.getAllCarritoInfo(id)
        return jsonify(result),201
    except Exception as e:
        return jsonify ({"Success":False, "message":str(e)}),500






