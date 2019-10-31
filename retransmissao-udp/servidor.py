# coding: utf-8
# udp

import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
orig = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.bind(orig)

TENTATIVAS_MAXIMAS = 3  # Numero de tentativas de reenvio por timeout
INTERVALO_TIMEOUT = 2   # Em segundos

def envia_msg(msg, dest, tentativas):
  if tentativas <= 0:
    udp.settimeout(None)
    print "Não foi possível enviar a mensagem. Número máximo de timeouts atingidos."
    return

  try:
    udp.sendto(msg, dest)
    udp.settimeout(INTERVALO_TIMEOUT)
    msg, cliente = udp.recvfrom(1024)
    while not (cliente == dest and msg == 'ACK'): msg, cliente = udp.recvfrom(1024)    
  except socket.timeout:
    print "Timeout! Tentando reenviar... Tentativas restates:", (tentativas - 1)
    envia_msg(msg, dest, tentativas - 1)

  udp.settimeout(None)

def recebe_msg():
  msg, cliente = udp.recvfrom(1024)
  udp.sendto('ACK', cliente)
  return msg, cliente

while True: 
  msg, cliente = recebe_msg()
  print "Recebido de %s: %s" % (cliente, msg)
  print "Enviando para %s: %s" % (cliente, msg)
  envia_msg(msg, cliente, TENTATIVAS_MAXIMAS)

udp.close()
