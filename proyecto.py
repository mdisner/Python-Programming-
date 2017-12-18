#!/usr/bin/python
import time
import sys
import re
import requests
import optparse
import socks
import socket
from urllib import urlopen
from urllib import FancyURLopener
from random import choice

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]


loscorreos = []
lossensibles = []
my_ip = 0
se = 0
ph = 0
roptions = 0
cms = 0
cmss = 0

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-s', '--servidor', dest='servidor', default=None, action="store_true", help='Analizes Server from headers')
    parser.add_option('-p', '--php', dest='php', default=None, action="store_true", help='Analizes the PHP version from headers')
    parser.add_option('-m', '--metodos', dest='metodos', default=None, action="store_true", help='Return the HTTP Methods')
    parser.add_option('-c', '--cms', dest='cms', default=None, action="store_true", help='Return CMS')
    parser.add_option('-i', '--email', dest='email', default=None, action="store_true", help='Shows all emails in a Web Page')
    parser.add_option('-L', '--archivos', dest='archivos', default=None, help='List with possible sensitive files')
    parser.add_option('-R','--reporte', dest='reporte', default=None, help='Archivo donde se guardara el reporte')
    parser.add_option('-t', '--tor', dest='tor', default=None, action="store_true", help='Make request with TOR')
    opts,args = parser.parse_args()
    return opts

def tiempo():
    print "\nEl ataque se realiza  " + time.strftime("%c")

def tor(options):
    if options.tor != None:
       socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
       socket.socket = socks.socksocket
       global my_ip
       my_ip = urlopen('http://ip.42.pl/raw').read()
       print "Se utiliza TOR con la IP", my_ip
    else:
       print "Precaucion, NO UTILIZAS TOR"
       pass


def servidor(options):
 if options.servidor != None:
    r = requests.get("http://www.ingenieria.unam.mx")
    global se
    se = r.headers['server']
    print "El servidor empleado es: ", r.headers['server']
 else: 
    pass


def php(options):

  if options.php != None:
     r = requests.get("http://www.ingenieria.unam.mx")
     global ph
     ph = r.headers['x-powered-by']
     print "La version de PHP utilizada es: ", r.headers['x-powered-by']
  else:
     pass

def metodos(options):

    if options.metodos != None:
       global roptions
       roptions = requests.options("http://www.ingenieria.unam.mx")
       print "Los metodos de HTTP son: ", roptions
    else:
       pass


def cms(options):
    
    if options.cms != None:
       global cms
       cms = requests.get("http://www.constantinm.co.uk")
       global cmss
       cmss = cms.headers['x-wix-renderer-server']
       print "El CMS es: ", cms.headers['x-wix-renderer-server']
    else:
       pass

def email(options):
    if options.email != None:
       correo = requests.get("http://www.seguridad.unam.mx")
       for email in re.findall("[\._\-a-z0-9]+\@[a-z0-9]+\.[a-z]+\.[a-z]*",correo.content):
           loscorreos.append(email)
           print "Se encontron las siguiente direcciones email: ", email
    else:
       pass

def archivos(options, file_lista):

 if options.archivos != None:
   with open (file_lista) as inputfile:
  
      for line in inputfile:
        a = line[:-1]
        url = "http://www.eldeforma.com/" + line[:-1]
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
           lossensibles.append(a)
           print "Se encuentra el archivo:", a
        else:
           pass
 else:
      pass 

def reporte(options, file_rep):

    if options.reporte != None:
       f=open(file_rep,'a')
       f.write("\n\n\nEl ataque se realizo  " + time.strftime("%c"))
       f.write("\nUtilizaste la IP %s\n" % my_ip)
       f.write("El servidor empleado es %s\n" % se)
       f.write("La version de PHP utilizada fue %s\n" % ph)
       f.write("Los metodos HTTP fueron %s\n" % roptions)
       f.write("El CMS hallado fue %s\n" % cmss)
       f.write("Los documentos sensibles hallados fueron:\n")
       for sensible in lossensibles:
           f.write("%s\n" % sensible)
       f.write("Los correos hallados fueron: \n")
       for email in loscorreos:
           f.write("%s\n" % email)
       f.close()
       print "El reporte fue guardado"
    else:
       print "No se guardara ningun reporte"


if __name__ == '__main__':
    try:
        opts = addOptions()
        tiempo()
        tor(opts)
        servidor(opts)
        php(opts)
        metodos(opts)
        cms(opts)
        email(opts)
        archivos(opts, opts.archivos)
        reporte(opts, opts.reporte)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)




