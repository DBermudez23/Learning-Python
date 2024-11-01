# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:34:14 2024

@author: User
"""

#Programa que imprima el factorial de un valor de la variable a, sin modificar la variable a durante el codigo

a = 4 
acc = a

for f in range (2, a):
    acc *= a
#print (acc)


#Escribe un programa que itere sobre una lista de nombres, dentro del bucle, si el nombre es 'judas' el programa debe escribir u texto acompañado del nombre diciendo 'es culpable', si no debera hacer lo mismo con el texto 'es inocente'

nombres = ['Pedro', 'Alonso', 'Judas', 'Sebastian', 'Santiago']
for nombre in nombres:
    if nombre == 'Judas':
        print (nombre, ' es culpable')
    else:
        print (nombre, ' es inocente')
        
#Modifica el codigo para el cálculo de un número primo usando la anidación de bucles para obtener de forma automatica números primos menores a 1000. Aprovecha la opción de usar else para mostrar solo números primos.

for num in range (1000):
    for div in range (2, num):
        if num % div == 0:
            break
    else:
        print (num)