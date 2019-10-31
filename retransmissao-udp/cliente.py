# coding: utf-8
import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
dest = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

TENTATIVAS_MAXIMAS = 3  # Numero de tentativas de reenvio por timeout
INTERVALO_TIMEOUT = 2   # Em segundos

def envia_msg(msg, dest, tentativas):
  if tentativas <= 0: 
    udp.settimeout(None)
    print "Não foi possível enviar a mensagem. Número máximo de timeouts atingidos."
    return

  try:
    udp.sendto(msg, dest)
    udp.settimeout(2)
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

print 'Para sair use CTRL+X\n'
msg = ''
while msg <> '\x18':
  msg = raw_input('Digite a mensagem: ')
  envia_msg(msg, dest, TENTATIVAS_MAXIMAS)
  resposta, cliente = recebe_msg()
  print "Recebido de volta:", resposta
udp.close()
