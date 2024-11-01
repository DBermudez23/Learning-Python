# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:42:43 2024

@author: User
"""

#Campos o keys de el diccionario contacto
campos = ('nombre', 'apellidos', 'email', 'telefono')

#Lista para almacenar los contactos, es decir, almacena multiples diccionarios con información de contactos
contactos = []

#Variable inicializada en s, sirve para revisar continuidad de ciclo while
seguir = 's'

#Ciclo que va a pedir por entrada, los valores que tomaran los key de la tulpa campos y los almacenara en un diccionario, cada diccionario representa un usuario
while seguir in ('s', 'S'):
    #Aca almacenaremos la información del contacto
    contacto = {}
    
    for campo in campos:
        valor = input(campo + ':')
        
        if len(valor) > 0:
            contacto[campo] = valor
    
    #Añadimos el contacto a la lista de contactos
    contactos.append(contacto)
    
    #Consulta al usuario si desda ingresar otro contacto haciendo uso de la variable seguir
    seguir = input('¿Introducir otro contacto? s/n: ')
    
#imprimimos uno a uno los contactos separados por guiones    
for contacto in contactos:
    for k, v in contacto.items():
        print(k + ':' + v)
    print('-------------------------')

#Almacenamos el numero de contactos que tienen email, recorriendo la lista de diccionarios y verificando si 'email' tiene algun valor almacenado
contador = len([c for c in contactos if 'email' in c])
print('El número de contactos almacenados es de: ', len(contactos))
print('el número de contactos que cuentan con email es de: ', contador)


"""
UNA VEZ INGRESADOS LOS DATOS ¿QUE CODIGO DE UNA SOLA LINEA NOS PERMITE ASIGNAR AL PRIMER CONTACTO LOS MISMOS VALORES ASIGNADOS AL ÚLTIMO?
"""
print(contactos[0])
contactos[0] = contactos[len(contactos)-1]

#Forma más efectiva:
contactos[0].update(contactos[-1])
print(contactos[0])


"""
ESCRIBIR EL CÓDIGO PARA MOSTRAR LOS DATOS DEL USUARIO CUYO CORREO ELECTRÓNICO HAYA SIDO INTRODUCIDO POR TECLADO. SI NO EXISTE ALGUNO CON ESE CORREO ELECTRONICO SE MOSTRARÁ EL MENSAJE 'NO ENCONTRADO'
"""

solicitud = input('Desea buscar los datos de un contacto a partir de su correo electronico? s/n')

while solicitud in ('s', 'S'):
    email = input('Ingrese el correo electronico de el contacto: ')
    for contacto in contactos:
        if email == contacto.get('email'):
            print('Contacto encontrado: ')
            for k, v in contacto.items():
                print(k, ' : ', v)
                break
        else:
            print('Contacto no encontrado')
                
    solicitud = input('¿Desea buscar otro contacto? s/n')