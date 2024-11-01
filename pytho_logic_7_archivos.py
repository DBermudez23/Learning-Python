# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:20:44 2024

@author: User
"""

lista_capitulos = [('capitulo 1', 'los niños y la programacion'),('capitulo 2', 'Introducción a la programación'),('capitulo 3', 'El lenguaje python y por que debemos aprenderlo')]

#PROGRAMA A DEBERA ESCRIBIR EL CONTENIDO DE LA LISTA EN UN ARCHIVO DE TEXTO, CERRARLO Y POSTERIORMENTE ABRIRLO PARA LEER SU CONTENIDO Y GENERAR UNA LISTA CON LA MISMA ESTRUCTURA

with open ('ejercicio_archivos1.txt', 'w') as f:
    for capitulo, titulo in lista_capitulos:
        f.write(capitulo + ' - ' + titulo + '\n')

lista_generada = []
with open ('ejercicio_archivos1.txt', 'r') as f:
    #f.readlines()genera una lista con el contenido del archivo
    for linea in f.readlines():
        #Eliminamos \n con .strip()
        #Separamos los elementos con un guion haciendo uso de .split()
        capitulo, titulo = linea.strip().split('-')
        lista_generada.append((capitulo, titulo))

print(lista_generada)


#PROGRAMA B DEBERA ESCRIBIR EL CONTENIDO DE LA LISTA EN UN ARCHIVO BINARIO, CERRARLO, POSTERIORMENTE ABRIRLO PARA LEER SU CONTENIDO Y GENERAR UNA LISTA CON LA MISMA ESTRUCTURA, SE DEBE HACER USO DE EL MODULO PICKLE

import pickle

with open('ejercicio_archivos2.txt', 'wb') as f:
    pickle.dump(lista_capitulos, f)
    
with open('ejercicio_archivos2.txt', 'rb') as f:
    lista_generada2 = pickle.load(f)
    
print(lista_generada2)