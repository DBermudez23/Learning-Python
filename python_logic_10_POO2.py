# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:47:31 2024

@author: User
"""

"""IMPLEMENTAR UN METODO EN LA CLASE HUERTO LLAMADO resumen(cosecha) QUE MUESTRE CUANTOS FRUTOS DE CADA TIPO SE HAN RECOLECTADO TOMANDO COMO ARGUMENTO EL RESULTADO DE huerto.recolectar()"""

class Planta():
    """Clase planta, con atributos básicos"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.altura = 0
        self.agua = 0
    
    def regar(self):
        self.agua += 1
        
    def crecer(self):
        """Crecimiento de una semana"""
        pass
    
    def recolectar(self):
        """Lista de frutos que produce"""
        pass
    
    def __str__(self):
        return f"{self.nombre} ({self.altura} cm)"

class Tomatera(Planta):
    
    def __init__(self):
        super().__init__('Tomatera')
        
    def crecer(self):
        """Tomatera crece 3 cm por unidad de agua"""
        self.altura += self.agua*3
        self.agua = 0
        
    def recolectar(self):
        """Tomatera da un fruto cada 10 cm después de 20 cm de altura"""
        if self.altura > 20:
            return['tomate'] * int(self.altura / 10)
        return []
    
class Habas(Planta):
    
    def __init__(self):
        super().__init__('Habas')
        
    def crecer(self):
        """La haba crece 5cm por unidad de agua"""
        self.altura += self.agua * 5
        self.agua = 0
    
    def recolectar(self):
        """La haba da un fruto cada 5 cm luego de 10 cm de altura"""
        if self.altura > 10:
            return ['haba'] * int(self.altura/5)
        return[]
    
class Huerto:
    """Clase huerto, contiene plantas"""
    __max__plantas = 10
    
    def __init__(self):
        self.__plantas = []
    
    def plantar(self, planta):
        if len(self.__plantas) >= self.__max__plantas:
            print('No queda suelo disponible')
        else:
            self.__plantas.append(planta)
    
    def regar(self):
        for m in self.__plantas:
            m.regar()
    
    def crecer(self):
        for m in self.__plantas:
            m.crecer()
            
    def recolectar(self):
        cosecha = []
        for m in self.__plantas:
            cosecha +=  m.recolectar()
        return cosecha
    
    def resumen(self, cosecha):
        """Metodo para generar un resumen de la cosecha"""
        d = {} #se genera diccionario
        for k in cosecha:#se recorre la lista que contiene los frutos para su respectivo conteo
            d[k] = d.get(k, 0) + 1 # se incrementa el contador
        for k in d: #Se recorre el diccionario para mostrar el resultado
            print(f'{d[k]} de: {k}')
    
    def __str__(self):
        msj = f'Hay {len(self.__plantas)} en el huerto: \n'
        for p in self.__plantas:
            msj += str(p) + '\n'
        return msj
    

if __name__ == '__main__':
    tomatera1 = Tomatera()
    tomatera2 = Tomatera()
    tomatera3 = Tomatera()
    habas1 = Habas()
    habas2 = Habas()
    
    huerto = Huerto()
    huerto.plantar(tomatera1)
    huerto.plantar(tomatera2)
    huerto.plantar(tomatera3)
    huerto.plantar(habas1)
    huerto.plantar(habas2)
    
    for i in range(67):
        huerto.regar()
        huerto.crecer()
        cosecha = huerto.recolectar()
        
    print(huerto.resumen(cosecha))