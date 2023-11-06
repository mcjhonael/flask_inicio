#de la libreria flask importame su clase Flask

from flask import Flask

app=Flask(__name__)

#decorador permite modificar el funcionamiento de una clase o una funcion en particular

@app.route('/contacto',methods=["GET"])
def contacto():
    return "hola desde aqui backend"


if (__name__=="__main__"):
    app.run(debug=True,port=5000)