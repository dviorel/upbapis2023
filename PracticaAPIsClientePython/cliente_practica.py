import requests
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta

class HistorialModel:
    def __init__(self, id, fecha: datetime.date, producto: str, precio: float):
        self.id = id
        self.fecha = fecha
        self.producto = producto
        # self.precio = float(precio)
        self.precio = float(precio)

    def __repr__(self):
        return f'HistorialModel: id={self.id}, fecha={self.fecha}, producto={self.producto}, precio={self.precio}'


def call_api(url, producto, fecha):
    response = requests.get(f'{url}?producto={producto}&fecha={fecha}')
    if response.status_code == 200:
        respuesta = response.json()
        historial = HistorialModel(**respuesta)
        return historial
    return None


def practica(url, productos, fecha_inicial, fecha_final):
    for producto in productos:
        fecha = fecha_inicial
        x = []
        y = []
        while fecha <= fecha_final:
            respuesta = call_api(url, producto, fecha)
            x.append(fecha)
            y.append(respuesta.precio)
            # fecha = fecha + timedelta(days=1, hours=6)
            # print(f'Iterando para {producto} con fecha {fecha}, respuesta={respuesta}')
            fecha = fecha.replace(year=fecha.year + 1)
        plt.plot(x, y, label=producto, marker='o')
    plt.xlabel('Fechas')
    plt.ylabel('Precio')
    # plt.ylim(15, 0)
    plt.title('Historial de precios')
    plt.legend()
    plt.show()



url = 'http://127.0.0.1:5000/historial_orm'
productos = ['Coca Cola 2l', 'Coca Cola 500 ml', 'Coca Cola 3l']
fecha_inicial = datetime.date(2012, 1, 10)
fecha_final = datetime.date(2023, 1, 10)


practica(url, productos, fecha_inicial, fecha_final)

