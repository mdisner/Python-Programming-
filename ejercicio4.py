#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo1 import Becario

calificacion_alumno = []
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        b1 = Becario(b,choice(calificaciones))
	calificacion_alumno.append(b1)



asigna_calificaciones()
for b in calificacion_alumno:
   print b 
