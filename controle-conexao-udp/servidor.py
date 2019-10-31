# coding: utf-8
# udp

import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
orig = (HOST, PORT)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.bind(orig)

def trata_conexao(cliente):
  while True:
    msg, _cliente = udp.recvfrom(1024)
    if _cliente == cliente:
      # Realiza ação, para esse caso vamos apenas retornar a msg
      udp.sendto(msg, cliente)
    # Tratar fim da conexao


def cria_conexao(cliente):
  udp.sendto('SYN-ACK', cliente)
  # start_timer()
  msg, _cliente = udp.recvfrom(1024)
  while _cliente != cliente: msg, _cliente = udp.recvfrom(1024)
  if msg == 'ACK':
    print "Conectado com %s! Pronto para receber dados." % cliente[0]
    trata_conexao(cliente)
  # se o timer estourar, sai da função

while True:
  msg, cliente = udp.recvfrom(1024)
  if msg == 'SYN': cria_conexao(cliente)
  if not msg: break

udp.close()
