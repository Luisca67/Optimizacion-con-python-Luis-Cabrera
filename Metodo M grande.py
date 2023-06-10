#Se importa la libreria
from pulp import *

#Se crea el problema de minimización
probl = LpProblem("Metodo M grande", LpMinimize)

#Se definen las variables de decisión
X = LpVariable("X", lowBound=0)
Y = LpVariable("Y", lowBound=0)

#Se define la función objetivo
probl += 6*X + 2*Y

#Se definen las restricciones
probl += 0.5*X + 0.2*Y <= 4
probl += 2*X + 3*Y >= 20
probl += 1*X + 1*Y == 10

#Se resuelve el problema a través de la funcion solve
probl.solve()

#Se muestra si la solucion es optima o no
print("Estado de la solución:", LpStatus[probl.status])

#Se muestran los resultados
print("Valor óptimo de X:", value(X))
print("Valor óptimo de Y:", value(Y))
print("Valor óptimo de Z:", value(probl.objective))