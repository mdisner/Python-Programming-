#!/usr/bin/python


dicc = []
raros = ["$#$", "$%", "&%$#", "&%/", "-.-", "..--//", "o/" ]

with open ('palabras') as inputfile:
  
      for line in inputfile:
        a = line[:3]
        dicc.append(a)
        for i in dicc:
            z = a+i
            for x in range(1,1000):
                
                for g in raros:
                  
                  
                  f=open('eldiccionario.txt','a')
                  print g+str(x)+z
                  print g+str(x)+line
                  print g+str(x)+line.title()
                  print g+str(x)+line.upper()
                  print g+str(x)+z[::-1]
                  print g+str(x)+line[::-1]
                  print g+str(x)+line.title()[::-1]
                  print g+str(x)+line.upper()[::-1]
                  f.write(g+str(x)+z)
                  f.write('\n')
                  f.write(g+str(x)+line)
                  f.write('\n')
                  f.write(g+str(x)+line.title())
                  f.write('\n')
                  f.write(g+str(x)+line.upper())
                  f.write('\n')
                  f.write(g+str(x)+z[::-1])
                  f.write('\n')
                  f.write(g+str(x)+line[::-1])
                  f.write('\n')
                  f.write(g+str(x)+line.title()[::-1])
                  f.write('\n')
                  f.write(g+str(x)+line.upper()[::-1])


                  f.close()                   

                





















