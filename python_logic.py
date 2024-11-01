# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 07:46:27 2024

@author: User
"""

#Mi coche gasta 5,5 litros cada 100km y mi trabajo se encuentra a 15km ¿Cuanto gastare de gasolina en 20 días laborales si el precio es de 1,12$/1?

distancia_trabajo = 2 * 15 * 20
gasto_coche = distancia_trabajo / 100 * 5.5
precio_litro = 1.12

precio_total = gasto_coche * precio_litro

#En enero del año actual tenia 3000 en la cuenta, si cobro 1100 mensuales y tengo gastos fijos de 435 ¿ a cuanto ascienden mis gastos extra mensuales si al final del año mi cuenta tiene un total de 6000?

saldo_actual = 3000
ingreso_mensual = 1100
gastos_fijos = 435
saldo_final = 6000

gastos_extras_anual = ((saldo_actual + ingreso_mensual * 12) - gastos_fijos * 12 ) - saldo_final

gastos_extras_mensual = gastos_extras_anual / 12

#Tengo 50$ para comprar una camisa. Si la camisa cuesta 35$ y tiene un descuento del 10% ¿Cuanto dinero tendre luego de comprar la camisa?

dinero_actual = 50
costo_camisa = 35 - (35 * .1)

dinero_restante = dinero_actual - costo_camisa

print (dinero_restante)