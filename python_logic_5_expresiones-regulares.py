# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:44:12 2024

@author: User
"""
#En este archivo veremos el uso de expresiones regulares con python

import re

cad = "Las expresiones regulares  jaamas jaaajajajaja jaaa son \tmuy\t potentes"


#Declaración de una expresión regular la cual busca palabras que empiecen por j o J seguidas de un caracter a o A, el {2,} indica que debe haber al menos 2 caracteres a o A para, es decir dos ocurrencias consecutivas sin un limite superior, el \w indica que estara seguido por cualquier caracter que le presiga, estas son las palabras que buscara
regex_multiples_a = re.compile(r'[jJ][aA]{2,}\w')

lista_coincidencias = re.findall(regex_multiples_a, cad)

if len(lista_coincidencias) > 0:
    print('Palabras que empiezan por ja con 2 o más a repetidas:')
    for coincidencia in lista_coincidencias:
        print('\t'+ coincidencia)
else:
    print('No hay palabras que empiecen por ja con más de 2 ´a´ seguidas')
    

"""
Programa que permita comprobar si las fechas de una lista son válidas o no, para que una fecha sea valida debera tener la estructura dd/mm/aaaa y
debera ser un valor comprendido entre 1990 y 2024
"""

lista_fechas = ['12/08/2020', '03/12/1998', '45/02/2025', '02/06/2024']

fecha_valida = re.compile(
    '''
    ^ #Aseguramos que la cadena comience en la fecha
    (0[1-9]|[12][0-9]|3[01]) #Especificamos para formato dd
    /
    (0[1-9]|1[0-2]) #Especificamos para formato mm
    /
    (19\d\d|20[0-2][0-9]) #Especificamos para formato aaaa entre 1900 y 2029
    $ #Aseguramos que la cadena termine en la fecha
    '''
    ,
    re.X)


for fecha in lista_fechas:
    if re.search(fecha_valida, fecha):
        print('La fecha: ', fecha, ' es valida\n')
    else:
        print('La fecha: ', fecha, ' es invalida\n')


"""
Escribe una expresión regular que permita extraer todas las palabras que terminen en os o as o sus equivalentes en mayúscula usando banderas
"""


expresion_regular = re.compile(r'\w*os| \w*as', re.I)

cadena_ejemplo = "complicados los amos y amas del señor"

validacion = re.findall(expresion_regular, cadena_ejemplo)

print(validacion)



"""
Escribe un programa para reemplazar por "x" los números de 
telefono de los clientes de una compañia que aparezcan en un texto
teniendo el formato xxx-xxx-xxx
"""

cadena_numeros = "El cliente ha especificado su correo electronico y numero de linea el cual es 123-123-123 y el de su madre el cual es 222-333-444"

identificador = re.compile(r'\d{3}-\d{3}-\d{3}')

censurado_telefono = re.sub(identificador, "xxx-xxx-xxx", cadena_numeros)

print(censurado_telefono)

    
