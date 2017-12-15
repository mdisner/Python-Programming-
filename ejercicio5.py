#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas

lisfin = (lambda lis1,lis2,lis3,lis4: lis1 + lis2 +lis3 + lis4)(sistemas,op_interna,incidentes,auditorias)

print lisfin
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
iii = filter(lambda nombre: 'i' in nombre, lisfin)

print iii

# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

mayus = map(lambda nombre: nombre.upper(), iii)

print mayus

