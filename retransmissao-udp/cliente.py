# coding: utf-8
import socket, rdt

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
dest = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print 'Para sair use CTRL+X\n'
msg = raw_input('Digite a mensagem: ')
while msg <> '\x18':
  rdt.send(udp, msg, dest)
  resposta, cliente = rdt.recv(udp)
  print "Recebido de volta:", resposta
  msg = raw_input('Digite a mensagem: ')
udp.close()
