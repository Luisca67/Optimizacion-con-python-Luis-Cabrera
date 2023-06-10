#Se importan la librerias
import numpy as np
import scipy.optimize as opt

#Se define la función objetivo, colocando los coeficientes
c = np.array([6, 2])  

#Se definen las restricciones
a = np.array([[1, 2], [3, 2]])  # Parte izquierda de las restricciones
b = np.array([4, 8])  # Parte derecha de las restricciones

#Se resuelve el problema a traves de la funcion linprog
resultado = opt.linprog(c=c, A_ub=-a, b_ub=-b, method='highs')

# Se imprimen los resultados
print('La solución óptima es:')
print('x =', resultado.x[0])
print('y =', resultado.x[1])
print('Z =', resultado.fun)
