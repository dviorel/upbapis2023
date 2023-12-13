from flask import Flask, jsonify
from flask_restful import Resource, Api, request
from db_direct import read_historial

app = Flask('Practica APIs Python')
api = Api(app)


class HistorialModel:
    def __init__(self, id, fecha, producto, precio):
        self.id = id
        self.fecha = fecha
        self.producto = producto
        self.precio = precio

    def __repr__(self):
        return f'Historial: id = {self.id}, fecha={self.fecha}, producto={self.producto}, precio={self.precio}'


class HistorialResource(Resource):
    def get(self):
        producto = request.args['producto']
        fecha = request.args['fecha']
        resultado = []
        items = read_historial(producto, fecha)
        for item in items:
            # resultado.append(vars(HistorialModel(item[0], item[1], item[2], item[3])))
            resultado.append(HistorialModel(item[0], item[1], item[2], item[3]).__dict__)
        print(f'items: {items}')
        print(f'items type: {type(items)}')
        print(f'items dir: {dir(items)}')
        return jsonify(resultado)


api.add_resource(HistorialResource, '/historial')
app.run()
