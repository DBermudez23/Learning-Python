# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:50:14 2024

@author: User
"""

"""SCRIPT QUE IMPORTE MODULO CADENAS Y CONCATENE LAS PALABRAS 'coche', 'moto', 'bicicleta' Y LAS SEPARE USANDO ',' ANTES DE MOSTRAR LAS PALABRAS"""
import cadenas

if __name__ == '__main__':
    cadena1 = 'coche,'
    cadena2 = 'moto,'
    cadena3 = 'bicicleta'
    
    cadena_concatenada = cadenas.concatenar(cadena1, cadena2)
    cadena_concatenada = cadenas.concatenar(cadena_concatenada, cadena3)
    
    cadena_final = cadenas.dividir(cadena_concatenada, ",")
    
    print(cadena_final)
    #.join devuelve una cadena resultante de unir las cadenas del iterable
    print("La cadena final es: \n" + '\n'.join(cadena_final))