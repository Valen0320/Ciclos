# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:52:40 2021

@author: Valen
"""

print("SISTEMA DE NOTAS DE UN CURSO DE PROGRAMACIÓN")

#Entrada

numeroEst = int(input("Digite la cantidad de estudiantes del grupo: "))

# Declarar la variable que cotrola el ciclo

contadorRep = 0
cantidadEstAprob = 0
cantidadEstRepro = 0
sumaDefEst = 0
promedioDefEst = 0 
sumaDefEstAprob = 0
sumaDefEstRepro = 0
promedioEstAprob = 0
promedioEstReprob = 0
mayor = 0
menor = 0

#Proceso
# Iniciar ciclo

for i in range(numeroEst):
    # Lectura de las notas de cada estudiante
    nombreEst = input("Digite nombre del estudiante: ")
    notaUnoEst = float(input("Digite la nota del primer parcial del estudiante: "))
    notaDosEst = float(input("Digite la nota del segundo parcial del estudiante: "))
    notaTresEst = float(input("Digite la nota del tercer parcial del estudiante: "))
    
    # Calcular la definitiva de cada estudiante
    notaDef = (notaUnoEst+notaDosEst+notaTresEst)/3
    
    #
    sumaDefEst = sumaDefEst+notaDef
    print("La definitiva es: ",notaDef)
    
    if(notaDef>=3.0):
        cantidadEstAprob=cantidadEstAprob+1
        # Sumar las notas de los estudiantes que aprobaron
        sumaDefEstAprob=sumaDefEstAprob+notaDef
    else:
        cantidadEstRepro=cantidadEstRepro+1
        # Sumar las notas de los estudiantes que reprobaron
        sumaDefEstRepro=sumaDefEstRepro+notaDef
    
    # Incrementa la variable que controla el ciclo
    
    contadorRep = contadorRep+1
    
    # Fin ciclo
# Calcular el promedio del grupo
promedioDefEst = sumaDefEst/numeroEst

if (cantidadEstAprob>0):
    promedioEstAprob = sumaDefEstAprob/cantidadEstAprob
if (cantidadEstRepro>0):
    promedioEstReprob = sumaDefEstRepro/cantidadEstRepro
    
print("OTROS CALCULOS")
print("Cantidad de estudiantes que aprobaron: ",cantidadEstAprob)
print("Cantidad de estudiantes que reprobaron: ",cantidadEstRepro)
print("Promedio del grupo: ",promedioDefEst)
print("Promedio de estudiantes que aprobaron",promedioEstAprob)
print("Promedio de estudiantes que reprobron",promedioEstReprob)
print("Nota maxima: ",mayor)
print("Nota minima: ",menor)