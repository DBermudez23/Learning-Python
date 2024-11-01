# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:30:01 2024

@author: User
"""

"""IMPLEMENTACIÓN DE METODO DE ENCRIPTACIÓN CESAR, GENERAR LA FUNCIÓN PARA DESCIFRAR EL MENSAJE"""

def cifrar(mensaje):
    desp = 4
    cif ="".join([chr(ord(c) + desp) for c in mensaje])
    return cif

def descifrar(mensaje):
    desp = 4
    dec = "".join([chr(ord(c) - desp) for c in mensaje])
    return dec

mensaje = "Daniel"
print('Original:', mensaje)
cifrado = cifrar(mensaje)
print('Cifrado:', cifrado)
descifrado = descifrar(cifrado)
print('Descifrado:', descifrado)

"""AÑADIR FUNCION INTERCAMBIA A ALGORITMO DE ORDENAMIENTO BUBBLE SORT"""

def ordenar(l):
    def intercambia(l, j, i):
        a = l[j]
        l[j] = l[i]
        l[i] = a
    
    #Este for recorre de atras hacia delante
    for i in range(len(l)-1, 1, -1):
        for j in range (i):
            if l[j] > l[j + 1]:
                intercambia(l, j, j + 1)

l = [7, 3, 9, 5, 4, 2, 8, 10]
ordenar(l)
print(l)


""""CALCULAR SUMA DE ELEMENTOS DE UNA LISTA DE MANERA RECURSIVA"""

def sumaElementos(l):
    if len(l) == 0:
        return 0
    return l[0] + sumaElementos(l[1:])

print(sumaElementos(l))

""""USANDO LAMBDA Y MAP(), UNA LINEA DE CODIGO QUE CAMBIE A MAYÚSCULA LA PRIMER LETRA DE CADA ELEMENTO DE LA LISTA"""

lista = ['stark', 'lannister', 'vanhouten', 'simpson', 'moe']

mayuscula = list(map(lambda i: i.capitalize(), lista ))

print(mayuscula)