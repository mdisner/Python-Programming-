#!/usr/bin/python

palabra = raw_input("Dame la palabra ")
arbalap = palabra[::-1]
def pali(palabra):

   if palabra == arbalap:
     print "TRUE"
   else:
     print "FALSE" 
   
pali(palabra)
