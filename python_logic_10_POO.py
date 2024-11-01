# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:14:38 2024

@author: User
"""
"""PROGRAMACIÓN ORIENTADA A OBJETOS CON PYTHON
"""

""""CLASE TELEVISOR AÑADIENDO A SU CONSTRUCTOR LA PROPIEDAD modelo, SOBRECARGA LOS OPERADORES == Y != A TRAVES DE LOS METODOS ESPECIALES __eq__() Y __ne__() PARA QUE DOS OBJETOS DE TIPO TELEVISOR SE CONSIDEREN IGUALES SI SON EL MISMO MODELO O DISTINTOS EN CASO CONTRARIO"""
class Televisor():
    def __init__(self, modelo):
        self.__canal = 0
        self.__num_canales = 55
        self.__modelo = modelo
    
    def __ajusta_canal(self, canal):
        """Este componente deja el canal en el rango de canales (0-55)"""
        self.__canal = canal % self.__num_canales
        
    def siguiente_canal(self):
        self.__ajusta_canal(self.__canal + 1)
        
    def anterior_canal(self):
        self.__ajusta_canal(self.__canal - 1)
        
    def cambia_canal(self, canal):
        if canal > self.__num_canales:
            self.__canal = self.__num_canales - 1
        elif canal < 0:
            self.__canal = 0
        else: 
            self.__canal = canal
            
    def canal_actual(self):
        return self.__canal
    
    def __ne__(self, obj):
        """Sobrecarga del operador !="""
        return self.__modelo != obj.__modelo
    
    def __eq__(self, obj):
        """Sobrecarga del operador =="""
        return self.__modelo == obj.__modelo
        
    
tv1 = Televisor("samsung")

tv2 = Televisor("LG")

tv3 = Televisor("samsung")

"""AÑADE UN METODO A LA CLASE DISPOSITIVO QUE ENCIENDA TODOS LOS DISPOSITIVOS DE UNA LISTA DADA. EL PROTOTIPO DEL METODO SERIA enciende_dispositivos(lista_dispositivos)"""


class Dispositivo():
    """Clase dispositivos, para objetos conectados a la red"""
    def __init__(self, IP):
        self.IP = IP
        self.__encendido = False
        
    def __del__(self):
        """Destructor"""
        print("Destruyendo dispositivo en: ", self.IP)
    
    def encender(self):
        """Enciende el dispositivo"""
        self.__encendido = True
    
    def apagar(self):
        """Apagado del dispositivo"""
        self.__encendido = False
    
    def estado(self):
        """Genera una cadena con el estado actual del dispositivo"""
        mensaje = f"IP: {self.IP}\n"
        if self.__encendido == True:
            mensaje += 'Estado: encendido'
        else:
            mensaje += 'Estado: apagado'
        return mensaje
            
    def enciende_dispositivos(lista_dispositivos):
        for dispositivo in lista_dispositivos:
            dispositivo.encender()
    
    

lista_dispositivos = []
tablet = Dispositivo('2.4.3')
celular = Dispositivo('4.6.7')
computadora = Dispositivo('3.4.2')

lista_dispositivos.append(tablet)
lista_dispositivos.append(celular)
lista_dispositivos.append(computadora)

estado_tablet = tablet.estado()
estado_celular = celular.estado()
estado_computadora  = computadora.estado()
print(estado_tablet + '\n' + estado_celular + '\n' + estado_computadora)

Dispositivo.enciende_dispositivos(lista_dispositivos)

estado_nuevo_tablet = tablet.estado()
estado_nuevo_celular = celular.estado()
estado_nuevo_computadora = computadora.estado()
print('Luego de usar la función enciende_dispositivos(): \n' + estado_nuevo_tablet + '\n' + estado_nuevo_celular + '\n' + estado_nuevo_computadora)


    
    
    
    
    


