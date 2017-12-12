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

primos()   
