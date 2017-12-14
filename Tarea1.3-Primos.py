#!/usr/bin/python


print "Este programa imprime los primeros n numeros primos"
n = input("Dame la cantidad de numeros primos que deseas: ")
lista = [2]

def primos2():
 print lista[:n]
 
"""

Esta funcion se encarga de imprimir la cantidad de elementos n, solicitada por el usuario de la lista que contiene solo numeros primos resultantes de la funcion primos

"""

 
 
 

def primos():
   for x in range(2,10000): 
    for i in range(2,x):
     if x % i != 0:
       j = i + 1
       if j == x:
          lista.append(x)
       else:
          pass
     else:
       break
   primos2()
   
"""
Esta funcion itera cada numero del rango (2,10000) calculando el modulo respecto a cada numero anterior a este, si el modulo es distinto de cero, entonces a la variable j se le suma 1, si al final de la iteracion resulta que cada modulo fue distinto de cero se tendra que j es igual a x, en otras palabras, x es entonces un numero primo, por lo tanto se agrega a la lista llamada lista.
En caso contrario, si hay un numero tal que el modulo sea igual a cero, automaticamente se descarta dicho numero para entrar a la lista.

"""
      
primos()


