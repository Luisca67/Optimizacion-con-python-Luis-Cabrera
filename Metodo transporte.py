#Se importan las funciones de pulp
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus

#Se definen los datos del problema
silos = ['Silo1', 'Silo2', 'Silo3']
molinos = ['Molino1', 'Molino2', 'Molino3', 'Molino4']

oferta = {
    'Silo1': 15,
    'Silo2': 25,
    'Silo3': 10
}

demanda = {
    'Molino1': 5,
    'Molino2': 15,
    'Molino3': 15,
    'Molino4': 15
}

costos = {
    ('Silo1', 'Molino1'): 10,
    ('Silo1', 'Molino2'): 2,
    ('Silo1', 'Molino3'): 20,
    ('Silo1', 'Molino4'): 11,
    ('Silo2', 'Molino1'): 7,
    ('Silo2', 'Molino2'): 9,
    ('Silo2', 'Molino3'): 24,
    ('Silo2', 'Molino4'): 12,
    ('Silo3', 'Molino1'): 4,
    ('Silo3', 'Molino2'): 14,
    ('Silo3', 'Molino3'): 16,
    ('Silo3', 'Molino4'): 18
}

#Se crea el problema de minimizacion
probl = LpProblem("Metodo de transporte", LpMinimize)

#se crean las Variables de decisión
x = LpVariable.dicts("envios", (silos, molinos), lowBound=0, cat='Integer')

#Se define la función objetivo
probl += lpSum(costos[(silo, molino)] * x[silo][molino] for silo in silos for molino in molinos)

#Se definen las restricciones de oferta
for silo in silos:
    probl += lpSum(x[silo][molino] for molino in molinos) <= oferta[silo]

#Se definen las restricciones de demanda
for molino in molinos:
    probl += lpSum(x[silo][molino] for silo in silos) >= demanda[molino]

#Se resuelve el problema a traves de la funcion solve
probl.solve()

# Se imprime por pantalla la cantidad de camiones cargados hacia el molino
for silo in silos:
    for molino in molinos:
         print(f"Se envian {int(x[silo][molino].value())} camiones cargados desde {silo} hacia {molino}")

#Se muestra por pantalla el costo total de transporte
print("El costo total de transporte es : ", round(probl.objective.value(), 2))