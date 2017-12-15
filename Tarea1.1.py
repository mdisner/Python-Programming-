
palis = []
"""
En esta lista se incluyen todos los palindromos que contiene el archivo.
Cada linea del archivo file 1 es separa en palabras y si la palabra
es un palindromo, es decir, si word == word[::-1] entonces
la agrega a la lista palis e imprime el palindromo de mayor longitud
"""
f = open('file1','r')
for line in f:
    for word in line.split():

        if word == word[::-1]:
           palis.append(word)
        else:
           pass

print max(palis, key=len)
