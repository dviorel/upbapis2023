import requests


class HistorialModel:
    def __init__(self, id, fecha, producto, precio):
        self.id = id
        self.fecha = fecha
        self.producto = producto
        self.precio = precio

    def __repr__(self):
        return f'HistorialModel: id={self.id}, fecha={self.fecha}, producto={self.producto}, precio={self.precio}'


def call_api(url, producto, fecha):
    # response = requests.get('http://127.0.0.1:5000/historial_orm?producto=Coca Cola 2l&fecha=2024-01-10')
    response = requests.get(f'{url}?producto={producto}&fecha={fecha}')
    if response.status_code == 200:
        print(response.status_code)
        print('Text')
        print(response.text)
        print(type(response.text))
        print('Json')
        print(response.json())
        print(type(response.json()))
        respuesta = response.json()
        # historial = HistorialModel(respuesta['id'], respuesta['fecha'], respuesta['producto'], respuesta['precio'])
        # historial = HistorialModel(id=respuesta['id'], fecha=respuesta['fecha'], producto=respuesta['producto'],
        #                            precioX=respuesta['precio'])
        # historial = HistorialModel(fecha=respuesta['fecha'], id=respuesta['id'], precioX=respuesta['precio'],
        #                            producto=respuesta['producto'])
        historial = HistorialModel(**respuesta)
        # historial = HistorialModel(respuesta.id, respuesta.fecha, respuesta.producto, respuesta.precio)
        print(f'Respuesta en objeto: {historial}')


url = 'http://127.0.0.1:5000/historial_orm'
producto = 'Coca Cola 2l'
fecha = '2012-01-10'
call_api(url, producto, fecha)

