#Se importan las librerias
import numpy as np
import matplotlib.pyplot as plt

#Función objetivo
def fo(x, y):
    return 9000 * x + 1200 * y

#Restriccion 1
def restric1(x):
    return x - 20

#Restriccion 2
def restric2(y):
    return y - 10

#Restriccion 3
def restric3(x, y):
    return 3 * x + 4 * y - 12

#Se define el rango de valores para X y Y
x = np.linspace(0, 25, 150)
y = np.linspace(0, 15, 150)

#Se crea la malla de coordenadas
X, Y = np.meshgrid(x, y)

#Se evaluan las restricciones en la malla
restric1_valor = restric1(X)
restric2_valor = restric2(Y)
restric3_valor = restric3(X, Y)

#Se crea la figura 
plt.figure()

#Se rellena la región factible
region_factible = (restric1_valor <= 0) & (restric2_valor <= 0) & (restric3_valor >= 0)
plt.imshow(region_factible, extent=(0, 25, 0, 15), origin='lower', cmap='Blues', alpha=0.3)

#Se grafican las restricciones
plt.contour(X, Y, restric1_values, [0], colors='red', alpha=0.5, linewidths=2, label='X <= 20')
plt.contour(X, Y, restric2_values, [0], colors='red', alpha=0.5, linewidths=2, label='Y <= 10')
plt.contour(X, Y, restric3_values, [0, 100], colors='red', alpha=0.5, linewidths=2, label='3X + 4Y >= 12')

#Se coloca el punto de la solución óptima
optima_x = 20
optima_y = 10
optima_z = fo(optimal_x, optimal_y)
plt.plot(optima_x, optima_y, 'ro', label='Solución Óptima')
plt.text(optima_x + 0.5, optima_y, f'({optima_x}, {optima_y})', verticalalignment='bottom', horizontalalignment='left', color='red')

#Se etiquetan los ejes
plt.xlabel('Eje de las X')
plt.ylabel('Eje de las Y')

#Se limita el rango de los ejes
plt.xlim(0, 25)
plt.ylim(0, 12)

#Se crea la leyenda
plt.legend(title='Restricciones')
plt.gca().get_legend().get_title().set_color('grey')
plt.gca().get_legend().get_title().set_fontweight('bold')
plt.gca().get_legend().get_title().set_fontsize(12)

#Se muestra el gráfico y el valor optimo de Z
plt.show()
print("El valor optimo de Z es:",optima_z)