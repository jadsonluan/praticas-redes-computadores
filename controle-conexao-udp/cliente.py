import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
dest = (HOST, PORT)

def connect(udp, host):
  udp.sendto("SYN", host)
  resposta, servidor = udp.recvfrom(1024)
  # while servidor != host: resposta, servidor = udp.recvfrom(1024)
  if resposta != 'SYN-ACK': return False
  udp.sendto('ACK', host)
  return True

if connect(udp, dest):
  print 'Para sair use CTRL+X\n'
  while True:
    msg = raw_input()
    if not msg: break
    udp.sendto(msg, dest)

# while msg <> '\x18':
#   udp.sendto(msg, dest)
#   resposta, cliente = udp.recvfrom(1024)
#   print "SERVIDOR ", resposta
#   msg = raw_input()
udp.close()