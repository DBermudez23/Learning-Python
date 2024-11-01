# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:11:06 2024

@author: User
"""
#Programa que pide al usuario su edad y la edad de su mejor amigo. El programa mostrará en pantalla quien es el mayor de los dos

edad1 = input('Digite nombre y edad separados por un espacio en blanco: ')
edad2 = input('Digite nombre y edad separados por un espacio en blanco: ')

#Se copia el str en una list
listaEdad1 = edad1.split(' ')
listaEdad2 = edad2.split(' ')
#Copiamos los elementos de la lista a un dict para pasar a evaluar
dictEdad1 = {'nombre' : listaEdad1[0], 'edad' : listaEdad1[1]}
dictEdad2 = {'nombre' : listaEdad2[0], 'edad' : listaEdad2[1]}

if dictEdad1['edad'] > dictEdad2['edad']:
    print(dictEdad1['nombre'], 'es mayor a', dictEdad2['nombre'])
elif dictEdad2['edad'] > dictEdad1['edad']:
    print(dictEdad2['nombre'], 'es mayor a', dictEdad1['nombre'])
else:
    print(dictEdad1['nombre'], 'y', dictEdad2['nombre'], 'tienen la misma edad')
    
#----- forma más sencilla de hacerse:

nombre1, edad1 = input('Digite nombre y edad separados por un espacio en blanco: ').split()
nombre2, edad2 = input('Digite nombre y edad separados por un espacio en blanco: ').split()

edad1 = int(edad1)
edad2 = int(edad2)

if edad1 > edad2:
    print(f'{nombre1} es mayor a {nombre2}')
elif edad2 > edad1:
    print(f'{nombre2} es mayor a {nombre1}')
else:
    print(f'{nombre1} y {nombre2} tienen la misma edad')
    
#Realiza un programa que pida un número entero al usuario y muestre los cinco números siguientes justificados a la derecha.

numero = int(input('Ingrese un número: '))

print('Los siguientes números siguientes: ')
justificacion = numero + 5
for i in range(5):
    numero += 1
    print(str(numero).rjust(justificacion))
    
#Programa que calcule el area de un triangulo a partir de la base y la altura ingresados por el usuario. Mostrar la salida usando paso de valores como parametros, concatenación de cadenas de texto, operador %, funcion str.format() y f-strings

base = int(input('Ingrese la base de el rectangulo: '))
altura = int(input('Ingresa la altura de el rectangulo: '))

area = base * altura

#Salida usando paso de valores como parametros:
    
print('El área de el rectangulo con base: ', base, 'y altura de: ', altura, 'es de: ', area)

#Salida usando concatenación de cadenas de texto:

print ('El área de el rectángulo con base: ' + str(base) + ' y altura de: ' + str(altura) + ' es de: ' + str(area))

#Salida usando operador %:
    
print('El área de un rectángulo con base: %(ba)d y altura de: %(al)d es de: %(ar)f' %{'ba' : base, 'al' : altura, 'ar' : area})

print('El área de un rectangulo con base: %d y altura de: %d es de: %f' %(base, altura, area))

#Salida usando función str.format

print('El área de un rectangulo con base: {ba} y altura de: {al} es de: {ar}'.format(ba = base, al = altura, ar = area))

print('El área de un rectangulo con base: {0} y altura de: {1} es de: {2}'.format(base, altura, area))

#Salida usando f-strings

print(f'El área de un rectangulo con base: {base} y altura de: {altura} es de: {area}')