from flask import Flask
from flask_restful import Resource, Api
app = Flask('Hello App')
api = Api(app)
# Esto es un comentario


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}

    def put(self):
        return {'hello': 'world'}

    def delete(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
app.run()
