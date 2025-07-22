from flask import Blueprint,request,jsonify
from flasgger import swag_from
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
from Infraestructure.MetricsDecorator import monitor_endpoint


bp=Blueprint("carrito",__name__)
#Creamos una instancia de DB
db=DB()
db.crearPool()
pool=db.getPool()


#Creamos un adaptador de crear carrito
crearCarAdapter=CrearCarritoAdapter(pool)
#Creamos un adaptador de utils
utils= UtilsAdapter(pool)
#Caso de Uso Crear Carrito
createCarUseCase=CrearCarritoUseCase(crearCarAdapter,utils)
#Creamos adaptador de anadirProd
addProdAdapter=AnadirProdAdapter(pool)
#Caso de Uso anadir Producto
anadirProdUseCase=AnadirProductoUseCase(addProdAdapter,utils)
#Creamos adaptador de cambiar cantidad de prod
cambCantAdap=CambiarCantidadAdapter(pool)
#Creamos caso de uso de cambiar cantidad
cambCabtiUseCase=CambiarCantidadUseCase(cambCantAdap,utils)
#Creamos adaptador de eliminarProducto
elimProdAdapter=EliminarProductoAdapter(pool)
#Creamos el caso de uso
elimProdUseCase=EliminarProductoUseCase(elimProdAdapter,utils)
#Creamos adaptador de vaciar carrito
vaciarCarrAdap=VaciarCarritoAdapter(pool)
#Creamos el caso de uso de vaciar carrito
vaciarCarUseCase=VaciarCarritoUseCase(vaciarCarrAdap,utils)
#Creamos adaptador de ObtenerCarrito
obtCarritoAdap=ObtenerCarritoAdapter(pool)
#Creamos caso de uso de ObtenerCarrito
obtCarritoUseC=ObtenerCarritoUseCase(obtCarritoAdap,utils)

#Un carrito se crea cuando se crea un usuario
@bp.route("/carrito/create",methods=["POST"])
@monitor_endpoint("crear_carrito")
def crear_carrito():
    """
    Crear un nuevo carrito de compras
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - userDocument
            - docType
          properties:
            userDocument:
              type: string
              description: Número de documento del usuario
              example: "1234567890"
            docType:
              type: string
              description: Tipo de documento (CC, TI)
              example: "CC"
              enum: ["CC", "TI"]
    responses:
      200:
        description: Carrito creado exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            message:
              type: string
              example: "Carrito creado exitosamente"
      409:
        description: Error en la creación (usuario ya existe)
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "El usuario ya tiene un carrito"
    """
    data=request.get_json()
    print(data)
    #Esta data se pasa al caso de uso encargado
    resul=createCarUseCase.crearCarrito(data.get("userDocument"),data.get("docType"))
    if(resul["Success"]):
        return jsonify(resul),200
    else:
        return jsonify(resul),409

#Añadir un nuevo producto al carrito
@bp.route("/carrito/addProduct",methods=["POST"])
@monitor_endpoint("add_product")
def add_product():
    """
    Añadir un producto al carrito
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - id_carrito
            - product_id
            - cantidad
          properties:
            id_carrito:
              type: integer
              description: ID del carrito
              example: 1
            product_id:
              type: integer
              description: ID del producto a añadir
              example: 123
            cantidad:
              type: integer
              description: Cantidad del producto
              minimum: 1
              example: 2
    responses:
      201:
        description: Producto añadido exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            message:
              type: string
              example: "Producto añadido exitosamente"
      500:
        description: Error interno del servidor
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "Error al añadir producto"
    """
    try:
        data=request.get_json()
        print(data)
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
@monitor_endpoint("change_quantity")
def cambiar_cantidad():
    """
    Cambiar la cantidad de un producto en el carrito
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - id_carrito
            - product_id
            - cantidad
          properties:
            id_carrito:
              type: integer
              description: ID del carrito
              example: 1
            product_id:
              type: integer
              description: ID del producto
              example: 123
            cantidad:
              type: integer
              description: Nueva cantidad del producto
              minimum: 1
              example: 3
    responses:
      201:
        description: Cantidad actualizada exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            message:
              type: string
              example: "Cantidad actualizada"
      400:
        description: Error en la solicitud
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "Producto no encontrado en el carrito"
      500:
        description: Error interno del servidor
    """
    data=request.get_json()
    id_carrito=data.get("id_carrito")
    id_prod=data.get("product_id")
    new_quantity=data.get("cantidad")
    try:
        prodServ=CommunicationProdService()
        prod=prodServ.obtainProductInfo(id_prod)
        resul=cambCabtiUseCase.cambiarCantidad(prod,new_quantity,id_carrito,id_prod)
        if(resul["Success"]):
            return jsonify(resul),201
        else:
            return jsonify(resul),400
    except Exception as e:
        return jsonify({"Success":False,"message":str(e)}),500


#Eliminar producto del carrito
@bp.route("/carrito/deleteProduct",methods=["DELETE"])
@monitor_endpoint("delete_product")
def delete_product():
    """
    Eliminar un producto del carrito
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - product_id
            - carrito_id
          properties:
            product_id:
              type: integer
              description: ID del producto a eliminar
              example: 123
            carrito_id:
              type: integer
              description: ID del carrito
              example: 1
    responses:
      201:
        description: Producto eliminado exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            message:
              type: string
              example: "Producto Eliminado del carrito"
      404:
        description: Producto no encontrado
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "Producto no encontrado en el carrito"
    """
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
@monitor_endpoint("vaciar_carrito")
def vaciar_carrito():
    """
    Vaciar completamente un carrito
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: id_carrito
        in: query
        required: true
        type: integer
        description: ID del carrito a vaciar
        example: 1
    responses:
      200:
        description: Carrito vaciado exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            message:
              type: string
              example: "Carrito vaciado con exito"
      400:
        description: ID de carrito no proporcionado
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "No se ha enviado un id de carrito para procesar la solicitud"
      500:
        description: Error interno del servidor
    """
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
@monitor_endpoint("get_carrito")
def get_carrito(id):
    """
    Obtener información completa de un carrito
    ---
    tags:
      - Gestión de Carrito
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID del carrito
        example: 1
    responses:
      201:
        description: Información del carrito obtenida exitosamente
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: true
            carrito:
              type: object
              properties:
                id_carrito:
                  type: integer
                  example: 1
                total:
                  type: number
                  format: float
                  example: 25.50
                items:
                  type: array
                  items:
                    type: object
                    properties:
                      product_id:
                        type: integer
                        example: 123
                      product_name:
                        type: string
                        example: "Producto ejemplo"
                      cantidad:
                        type: integer
                        example: 2
                      medida:
                        type: string
                        example: "KG"
                      total_prod:
                        type: number
                        format: float
                        example: 25.50
      404:
        description: Carrito no encontrado
        schema:
          type: object
          properties:
            Success:
              type: boolean
              example: false
            message:
              type: string
              example: "El carrito no existe"
      400:
        description: Error en la solicitud
      500:
        description: Error interno del servidor
    """
    try:
        result=obtCarritoUseC.getAllCarritoInfo(id)
        if(result.get("message")=="No existe"):
            return jsonify({"Success":False,"message":"El carrito no existe"}),404
        elif result["Success"]:
            return jsonify(result),201
        else:
            return jsonify(result),400
    except Exception as e:
        return jsonify ({"Success":False, "message":str(e)}),500

@bp.route("/carrito/getIdCarrito/<userdocument>/<doctype>",methods=["GET"])
def getIdCarrito(userdocument,doctype):
    try:
        print(userdocument,doctype)
        id_carrito=utils.obtenerIdCarrito(userdocument,doctype)[0]
        print(id_carrito)
        return jsonify({"Success":True,"id_carrito":id_carrito}),200
    except Exception as e:
        return jsonify({"Success":False,"message":"No fue posible obtener un id de carrito para este usuario"}),404







