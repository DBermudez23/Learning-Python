# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:36:51 2024

@author: User
"""

"""MANEJO DE ERRORES, EXCEPCIONES Y PRUEBAS UNITEST"""

"""ESCRIBE UN PROGRAMA QUE RECIBA COMO ENTRADA UNA LISTA DE VARIOS ELEMENTOS DE TIPO INT Y EL ÚLTIMO ELEMENTO DE TIPO STRING, RECORRE TODOS LOS ELEMENTOS DE LA LISTA Y CALCULA EL NUMERO FACTORIAL DE CADA ELEMENTO CON EL METODO DE EL MODULO MATH, MOSTRANDO EL RESULTADO POR CONSOLA SI NO SE PRODUCE NINGUNA EXEPCION. CAPTURA LAS EXCEPCIONES CONVENIENTES Y MUESTRA UN MENSAJE FINAL, INDICANDO EL VALOR QUE SE HA PROCESADO"""

from math import factorial

def factorial_lista(lista):
    for i in lista: 
        try:
            factorialNum = factorial(i)
        except TypeError:
            print("Error de tipo de dato en: ", i)
        except ValueError:
            print("Factorial unicamente acepta enteros positivos")
        else:
            print("El factorial de: ", i, "es: ", factorialNum)
        finally:
            print("Valor: ", i, "procesado")

lista = [2, 8, 5, 'Hola']
factorial_lista(lista)


"""CREAR UNA EXCEPCIÓN PROPIA PARA GESTIONAR LA DETECCION DE UNA CADENA INFERIOR A DOS CARACTERES EN UNA LISTA DE NOMBRES. ESCRIBE UN PROGRAMA QUE HAGA USO DE ESA EXCEPCION PARA EVITAR MOSTRARLA POR PANTALLA"""

class NombresRestrict(Exception):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        print("ERROR: Nombre con menos de 2 caracteres no se considera valido")
        
def validarNombres(lista_nombres):
    for i in lista_nombres:
        try:
            if len(i) < 2:
                raise NombresRestrict(i)
            print(i)
        except NombresRestrict:
            pass

lista_nombres = ['Daniel', 'po', 'Sofia', 'a', 'arracacha', 'b']
validarNombres(lista_nombres)

        
"""REALIZA PRUEBAS UNITARIAS UTILIZANDO assert PARA COMPROBAR SI LA SUGUIENTE FUNCION CALCULA CORRECTAMENTE EL FACATORIAL DE UN NÚMERO. EN CASO DE QUE HAYA ALGUN ERROR, INDICA CUAL ES LA SOLUCION CORRECTA"""

def factorial(num):
    if num == 0 or num ==2:
        return 1
    return num * factorial(num - 1)

resultado = factorial(0)
assert resultado == 1

#Aqui se genera un error
resultado = factorial(2)
assert resultado == 1

"""LA FUNCION formatea_mombre() PASA A MAYUSCULAS LA PRIMER LETRA DE CADA COMPONENTE DE UN NOMBRE COMPLETO, AÑADIR COMPROBACIONES PARA DISTINTOS CASOS"""

def formatea_nombre(nombre):
    return "".join([x[0].upper() + x[1:] for x in nombre])

import unittest

class Test(unittest.TestCase):
    def test_formatear(self):
        self.assertEqual(formatea_nombre('theon greyjoy'), 'Theon Greyjoy')
    def test_segundonombre(self):
        self.assertEqual(formatea_nombre('antonio muñoz molina'), 'Antonio Muñoz Molina')
    def test_tercernombre(self):
        self.assertEqual(formatea_nombre('ursula k. le guin'), 'Ursula K. Le Guin')
    def test_cuartonombre(self):
        self.asserEqual(formatea_nombre('calderon de la barca'), 'Calderon De La Barca')
    def test_quintonombre(self):
        self.assertEqual(formatea_nombre('alberto vazquez-figueroa'), 'Alberto Vazquez-figueroa')
    
    if __name__ == '__main__':
        unittest.main()
    

