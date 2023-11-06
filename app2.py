from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos=[
    {"nombre":"palta fuerte","precio":5.23},
    {"nombre":"tomati","precio":12.5},
    {"nombre":"cebolla","precio":7.5}
]

@app.route("/", methods=['GET'])
def home():
    return {
        "message": "Bienvenido ala API",
        "content": None
    }


@app.route("/productos", methods=['GET', 'POST'])
def gestion_productos():
    if request.method == "GET":
        return {
            "content": productos,
            "message": "lista de productos"
        },200
    if request.method == "POST":
        print(request.get_json()["nombre"])

        nombre=request.get_json()["nombre"]
        apellido=request.get_json()["apellido"]
        edad=request.get_json()["edad"]

        # print(f"nombre es {nombre}")
        # print(f"apellido es {apellido}")
        # print(f"edad es {edad}")
        # print("a tu mama le gusta {}".format(request.get_json()["fruta"]))
        print(f"lista de productos {productos}")
        producto=request.get_json()
        print(productos)
        productos.append(producto)
        print(productos)
        print()
        return {
            "message": "producto creado exitosamente",
            "content": producto
        },201
    
@app.route("/producto/<int:id>",methods=["GET","PUT","DELETE"])
def gestion_producto(id):
    total_productos=len(productos)
    if id<total_productos:
        if request.method=="GET":
            return{
                "content":productos[id],
                "message":None
            },200
        elif request.method=="PUT":
            data=request.get_json()
            productos[id]=data
            return {
                "message":"Producto actualizado exitosamente",
                "content":productos[id]
            },201
        elif request.method=="DELETE":
            del productos[id]
            return {
                "content":None,
                "message":"Producto eliminado"
            },200
    return {
        "content":None,
        "message":"Producto no encontrado"
    }

if __name__ == "__main__":
    app.run(debug=True, port=5000)
