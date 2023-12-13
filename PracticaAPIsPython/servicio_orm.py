from flask import Flask, jsonify
from flask_restful import Resource, Api, request
from flask_sqlalchemy import SQLAlchemy

app = Flask('Practica APIs Python')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
db = SQLAlchemy(app)
api = Api(app)


class HistorialModel(db.Model):
    __tablename__ = 'api_historial'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    producto = db.Column(db.String(50))
    precio = db.Column(db.Numeric)

    def as_dict(self):
        # a = getattr(self, 'abc')
        # a = self.abc
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    # def as_dict(self):
    #     return {'id': self.id, 'fecha': self.fecha, 'producto': self.producto, 'precio': self.precio}

    def __repr__(self):
        return f'Historial: id={self.id}, fecha={self.fecha}, producto={self.producto}, precio={self.precio}'


class HistorialResource(Resource):
    def get(self):
        producto = request.args['producto']
        fecha = request.args['fecha']
        item = HistorialModel.query.filter(HistorialModel.producto == producto, HistorialModel.fecha == fecha).first()
        print(f'items: {item}')
        print(f'items type: {type(item)}')
        print(f'items dir: {dir(item)}')
        return jsonify(item.as_dict())

    def post(self):
        datos = request.get_json()
        print(f'Datos recibidos: {datos}')
        item = HistorialModel()
        item.id = datos['id']
        item.producto = datos['producto']
        item.fecha = datos['fecha']
        item.precio = datos['precio']
        print(f'item a guardar: {item}')
        db.session.add(item)
        db.session.commit()
        return jsonify(item.as_dict())


api.add_resource(HistorialResource, '/historial_orm')
app.run()
