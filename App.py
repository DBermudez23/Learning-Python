# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:28:23 2024

@author: User
"""

from tkinter import *
import tkinter.ttk as ttk
from webfrec import *

max_frec = 20

def contar(*args):
    frec_items = contar_palabras(textcomp.get(1.0, END))
    for entry in tree.get_children():
        tree.delete(entry)
    for k,v in frec_items[:max_frec]:
        tree.insert("", "end", values=(k, v))

def descargar(*args):
    """Esta función se invoca al pulsar el boton descargar"""
    text = descargar_pagina(url.get())
    textcomp.replace(1.0, END, text)
    
    frec_items = contar_palabras(text)
    for entry in tree.get_children():
        tree.delete(entry)
    for k, v in frec_items[:max_frec]:
        tree.insert("", "end", values = (k, v))

root = Tk()
root.title("Analizador de paginas web")

#Marco principal----------------------------------------------------------
mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))

#Marco para dirección web y boton de descarga-----------------------------
    
urlframe = ttk.Frame(mainframe)
urlframe.grid(column=1, row=1, sticky=N, pady="5 0")
#Etiqueta
ttk.Label(urlframe, text="Direccion url:").grid(column=1, row=1, sticky=W)

#Boton de contar
button = ttk.Button(urlframe, text="Contar", command=contar)
button.grid(column=4, row=1, sticky=W, padx="5 0")

#Campo de dirección web---------------------------------------------------
url = StringVar()
urlentry = ttk.Entry(urlframe, width=83, textvariable=url)
urlentry.grid(column=2, row=1, sticky=W, padx="5 0")

#Boton de descargar-------------------------------------------------------
button = ttk.Button(urlframe, text="Descargar", command=descargar)
button.grid(column=3, row=1, padx="5 0")

#Marco para mostrar datos de la página------------------------------------
showframe = ttk.Frame(mainframe)
showframe.grid(column=1, row=2, pady="5 0")

ttk.Label(showframe, text="Texto:").grid(column=1, row=1, sticky=W)
ttk.Label(showframe, text="Tabla de frecuencias:").grid(column=2, row=1, sticky=W)

#Barra de desplazamiento para el área de texto
scrollbar = ttk.Scrollbar(showframe, command=textcomp.yview)
scrollbar.grid(column=2, row=2, sticky="wns")
textcomp['yscrollcomand'] = scrollbar.set

#Lienzo donde mostrar contenido
content = StringVar()
textcomp = Text(showframe, width=80, height=26)
textcomp.grid(column=1, row=2, sticky=W)

#Tabla donde se muestran las palabras más frecuentes
tree = ttk.Treeview(showframe, height=max_frec, columns=("pal", "frec"))
tree.grid(column=2, row=2, sticky=(W, N), padx="5 0")
tree.column("#0", width=0, minwidth=0, stretch=NO)
tree.column("pal", width=100, minwidth=100, stretch=NO)
tree.column("frec", width=70, minwidth=70, stretch=NO)
tree.heading("pal", text="Palabra", anchor=W)
tree.heading("frec", text="Frecuencia", anchor=W)

#Configuración final
urlentry.focus()
root.bind('<Return>', descargar)
root.resizable(width=False, height=False)
root.mainloop()
    