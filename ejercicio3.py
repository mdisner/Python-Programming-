#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

aprobadoslist = []
reprobadoslist = []
promediolist = []
calif = []
califics = []

calificacion_alumno = {}
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
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def aprobados():
    for alumno in calificacion_alumno:
      if calificacion_alumno[alumno] >= 8:
        aprobadoslist.append(alumno)
      else:
        reprobadoslist.append(alumno)

def promedio():
    for alumno in calificacion_alumno:
#       print calificacion_alumno[alumno]
        calif.append(calificacion_alumno[alumno])
      
    sum1 = sum(calif) 
    prom = float(sum1)/len(becarios)
    print "El promedio es %s" % prom

def imprime_calificaciones2():
    for alumno in calificacion_alumno:
        califics.append(calificacion_alumno[alumno])
    print califics


asigna_calificaciones()
imprime_calificaciones()
aprobados()
promedio()
imprime_calificaciones2()

aprobadoslist = tuple(aprobadoslist)
reprobadoslist = tuple(reprobadoslist)

print tuple(aprobadoslist)
print tuple(reprobadoslist)
