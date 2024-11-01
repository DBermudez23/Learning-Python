# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:24:13 2024

@author: User
"""

#Comprension de listas 

#Recorrer una lista buscando los elementos mayores a 25 para rebanarlos y añadirlos a otra lista
edades = [23, 34, 67, 25, 45, 27]
mayores = [x for x in edades if x > 25]
print('La cantidad de mayores a 25 años es: ', mayores)


#Recorrer dos listas para armar posibles parejas guardandolas en tuplas dentro de una lista (parejas_posibles)...
chicos = ['Juan', 'Alonso', 'Martin']
chicas = ['Estefa', 'Mariana', 'Sofia']
parejas_posibles = [(x, y) for x in chicos for y in chicas]
print(parejas_posibles)


#Recorrer una lista para armar posibles parejas para un debate escolar
alumnos = ['Santi', 'Dani', 'Luisa', 'Estefa', 'Sofi', 'Maria']
posibles_debates = [(alumnos[i], alumnos[j]) for i in range(len(alumnos)) for j in range(i+1, len(alumnos))]
print(posibles_debates)

#Generando una matriz de 4x4
l = [[x for x in range(i * 4, (i + 1) * 4)] for i in range(4)]
print(l)


#Escribe en una sola linea de codigo usando compresión como generar una lista con los nuúmeros pares del 0 al 99
l = [x for x in range(100) if x % 2 == 0]


#Programa que a partir de dos listas va evaluar cual fue el mes más lluvioso

lluvia_mensual = [65, 70, 56, 62, 44, 14, 5, 5, 24, 50, 57, 69]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

max_lluvia = max(lluvia_mensual)
mes_max = lluvia_mensual.index(max_lluvia)
print(f'El mes más lluvioso ha sido {meses[mes_max]} con {max_lluvia} litros')
