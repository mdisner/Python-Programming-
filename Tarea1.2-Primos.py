#!/usr/bin/python


print "Este programa valida si un numero entero es primo o no"
n = input("Dame el numero entero a evaluar: ")

def primos():

 for i in range(2, n): 
     if n % i != 0:
       j = i + 1
       if j == n:
          print "TRUE" 
          print "%s es un numero primo" % n
       else:
          pass
     else:
       print "FALSE"
       print "%s no es numero primo" % n
       break
       
"""
Esta funcion recibe un numero entero como valor, despues itera cada numero del rango (2,n) calculando el modulo respecto a cada 
numero anterior a este, si el modulo es distinto de cero, entonces a la variable j se le suma 1. 
Si al final de la iteracion resulta que cada modulo fue distinto de cero se tendra que j es igual a x, en otras palabras, 
x sera entonces un numero primo, por lo tanto se imprime un TRUE y se confirma que x es un numero primo.
En caso contrario, si hay un numero tal que el modulo sea igual a cero, automaticamente se descarta dicho numero y se imprime
FALSE.
"""        

primos()   
