# coding: utf-8
# udp
'''
CONCATENAR  a b   =>  a+b
COMPARAR    a b   => Igual/Diferente
SUBSTRING   w i f => w.substring(i, f) 
CONTEM      w c   => Sim/Nao
SUBSTITUIR  w a b => w.replace(a, b)
default           => Comando Invalido
'''

import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
orig = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.bind(orig)

def calculadora(entrada):
  splitted = entrada.split(' ')
  op = splitted[0]

  if op == 'CONCATENAR':
    return splitted[1] + splitted[2]
  elif op == 'COMPARAR':
    return 'Igual' if splitted[1] == splitted[2] else 'Diferente'
  elif op == 'SUBSTRING':
    inicio = int(splitted[2])
    fim = int(splitted[3])
    return splitted[1][inicio:fim]
  elif op == 'CONTEM':
    return 'Sim' if splitted[2] in splitted[1] else 'Nao'
  elif op == 'SUBSTITUIR':
    return splitted[1].replace(splitted[2], splitted[3])
  else:
    return "comando invalido"

while True:
  msg, cliente = udp.recvfrom(1024)
  if not msg: break
  udp.send(calculadora(msg))

udp.close()
