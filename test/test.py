# a = 12
a = 'Danny'
b = 3
print(a*b)

numbers = [1, -10, 0, -5, -1000, 100, 7]

maximum = numbers[0]

for number in numbers:
    if number > maximum or number > 0:
        maximum = number

print("The maximum value is", maximum)

def saludo(nombre: str):
    # print('Hola ' + nombre)
    print(f'Hola {nombre}')


def get_hello_world():
    pass


def _saludo(nombre):
    return f'Hola {nombre}'


nombre = 'Danny'
nombre = 30
saludo(nombre)
