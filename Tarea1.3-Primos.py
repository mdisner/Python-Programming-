#!/usr/bin/python


print "Este programa imprime los primeros n numeros primos"
n = input("Dame la cantidad de numeros primos que deseas: ")
lista = [2]

def primos2():
 print lista[:n]

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
primos()


