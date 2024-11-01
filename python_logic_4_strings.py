# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:26:51 2024

@author: User
"""

Escribe un programa que lea una cadena y compruebe si el primer y ultimo número son iguales, si son iguales, mostrara un mensaje con el numero total de caracteres distintos a dicho caracter, en caso contrario mostrara un mensaje con el número total de caracteres de la cadena iguales al caracter inicial y al caracter final (sin incluirlos)


cadena = input('Ingrese una cadena de texto para comparar sus caracteres: ')
cadena = cadena.lower()

if cadena[0] == cadena[-1]:
    caracteres_distintos = len(cadena) - cadena.count(cadena[0])
    print(f'La cadena comienza por {cadena[0]} y termina con {cadena[-1]}, el número de caracteres distintos a este es de: {caracteres_distintos}')
else:
    caracter_inicial = (cadena.count(cadena[0])) - 1
    caracter_final = (cadena.count(cadena[-1])) - 1
    print(f'La cadena comienza por {cadena[0]} y termina con {cadena[-1]}\n el número de veces que se repite el caracter "{cadena[0]}" es: {caracter_inicial}\n el número de veces que se repite el caracter "{cadena[-1]}" es: {caracter_final}')
    
    
#Utilizar los metodos split() y join() para sustituir el nombre de la cadena "mi nombre es Paula" por tu nombre

cadena_inicial = "Mi nombre es Paula"

cadena_lista = cadena_inicial.split()

cadena_lista[3] = 'Daniel'

cadena_inicial = ' '.join(cadena_lista)

print(cadena_inicial)

