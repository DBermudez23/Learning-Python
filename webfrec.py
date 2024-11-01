# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:59:38 2024

@author: User
"""

import requests
import html2text
import re

def descargar_pagina(url):
    """
    lee una página web y la convierte en texto plano
    """
    try:
        page = requests.get(url)
        content = html2text.html2text(page.text)
    except Exception:
        pass
    return content

def contar_palabras(texto):
    """
    Calcula la frecuencia de aparición de cada palabra en un texto y genera una lista de pares clave valor, ordenada de mayor a menor frecuencia    
    """
    frec = {}
    texto = re.sub('[^\w\s]+', '', texto) #eliminación de signos de puntuación y espacios, etc
    for w in texto.lower().split():
        if len(w) > 3: #Verifica que la palabra sea de más de 3 caracteres
            frec[w] = frec.get(w, 0) + 1
        #Se ordenan elementos de la lista generada a partir del diccionario, una lista de tuplay ya que se hizo uso de.items()
        frec_sorted = sorted(frec.items(), key=lambda x: x[1], reverse=True) 
        
    return frec_sorted
