# coding: utf-8
# udp

import socket
import rdt

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
orig = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.bind(orig)

while True: 
  msg, cliente = rdt.recv(udp)
  print "Recebido de %s: %s" % (cliente, msg)
  print "Enviando para %s: %s" % (cliente, msg)
  rdt.send(udp, msg, cliente)

udp.close()
