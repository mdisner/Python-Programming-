#!/usr/bin/python

import random

lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
global minus, mayus, nume
minus = 1
mayus = 1
nume = 1

def minusculas():
 min = input("Cuantas minusculas contendra tu contrasena: ")
 global minus
 minus = ''.join(random.sample(lista1, min))

 """
 Esta funcion recibe un numero entero (min) y selecciona aleatoriamente min cantidad de elementos de la lista1, por ultimo
 une en una cadena los caracteres.
 """
 
 
def mayusculas():
 may = input("Cuantas mayusculas contendra tu contrasena: ")
 global mayus
 mayus = ''.join(random.sample(lista2, may))

 """
 Esta funcion recibe un numero entero (may) y selecciona aleatoriamente may cantidad de elementos de la lista2, por ultimo
 une en una cadena los caracteres.
 """ 
 
 
 

def numeros():
 num = input("Cuantos digitos contendra tu contrasena: ")
 global nume
 nume = ''.join(random.sample(lista3, num))
 
  """
 Esta funcion recibe un numero entero (num) y selecciona aleatoriamente num cantidad de elementos de la lista3, por ultimo
 une en una cadena los caracteres.
 """


def final():
  
  minusculas()
  mayusculas()
  numeros()
  print minus+mayus+nume

 """
 Esta funcion simplemente concatena las cadenas generadas por las funciones anteriores para formar una contraseña segura
 y con complejidad 3.
 """  
  
final()
