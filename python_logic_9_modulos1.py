# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:06:48 2024

@author: User
"""

"""PROGRAMA QUE IMPRIMA POR PANTALLA TODOS LOS COMPONENTES DEL MODULO re TERMINADOS EN CH"""

import re

#Almacenamos en la variable componentes todos las componentes del modulo re
componentes = dir(re)

#Recorremos cada uno de los componentes
for componente in componentes:
    #Declaración de expresión regular que servira como patrón de busqueda
    regex_terminados_ch = re.compile(r'\w+ch\b')
    #Almacenamos en componentes_ch los componentes terminados en ch
    componentes_ch = re.findall(regex_terminados_ch, componente)
    #Recorremos la lista componentes_ch donde se almacenaron componentes coincidentes con lo requerido para imprimirlos en pantalla
    for i in componentes_ch:
        print('\t' + i)






