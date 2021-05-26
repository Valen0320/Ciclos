# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:25:38 2021

@author: Valen
"""

# Calcular el factorial de un numero N 
factorial = int(1);
num = int(input("Ingrese numero a calcula el factorial: "))

while (num!=0):
    factorial = factorial*num;
    num = num-1
print("El factorial del numero es: "+str(factorial))