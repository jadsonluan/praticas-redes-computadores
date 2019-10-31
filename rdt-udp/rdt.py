# coding: utf-8
import socket

__name__ = "rdt"

MAX_ATTEMPTS = 3  # Numero de tentativas de reenvio por timeout
TIMEOUT_INTERVAL = 2   # Em segundos

def send(udp, msg, dest):
  send_recursive(udp, msg, dest, MAX_ATTEMPTS)

def send_recursive(udp, msg, dest, attempts):
  if attempts <= 0:
    udp.settimeout(None)
    print "Não foi possível enviar a mensagem. Número máximo de timeouts atingidos."
    return

  try:
    udp.sendto(msg, dest)
    udp.settimeout(TIMEOUT_INTERVAL)
    msg, sender = udp.recvfrom(1024)
    while not (sender == dest and msg == 'ACK'): msg, sender = udp.recvfrom(1024)    
  except socket.timeout:
    print "Timeout! Tentando reenviar... Tentativas restates:", (attempts - 1)
    send_recursive(udp, msg, dest, attempts - 1)

  udp.settimeout(None)

def recv(udp):
  msg, sender = udp.recvfrom(1024)
  udp.sendto('ACK', sender)
  return msg, sender