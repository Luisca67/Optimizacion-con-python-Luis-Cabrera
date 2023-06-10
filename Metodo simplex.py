#Se importan las librerias
import numpy as np
from scipy.optimize import linprog

#Se define la función objetivo 
fo = np.array([110, 150])

#Se definen las restricciones
a = np.array([[4, 6], [20, 10]]) #Lado izquiero de las restricciones
b = np.array([480, 1500]) #Lado derecho de las restricciones

#Se utiliza la funcion linprog para resolver el problema, pasandole la fo y las restricciones
resultado = linprog(-fo, A_ub=a, b_ub=b, method='highs')

#Se imprimen los resultados

print("La soluciones optima del problema es:")

#Se redondean los resultados con round
print("x =", round(resultado.x[0], 2))
print("y =", round(resultado.x[1], 2))
print("Valor óptimo de la función objetivo: Z =", round(-resultado.fun, 2))