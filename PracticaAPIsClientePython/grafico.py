import matplotlib.pyplot as plt

# plt.plot(x, y, linestyle='-', marker='o', label=’’) # x & y son listas
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 9, 16, 25, 36, 49]
plt.plot(x, y, linestyle='--', marker='o', label='Funcion cuadratica')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('DEMO')
plt.legend()
plt.show()















