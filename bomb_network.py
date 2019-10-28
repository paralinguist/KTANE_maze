import socket
from select import select
import json
import sys

#TODO: when first connecting, request a GUID from server to register module (if within registration time)

INITIALISING = 0
ACTIVE = 1
DEFUSED = 2
EXPLODED = 3

leds_available = ['IBM', 'CAR', 'RAC', 'LIT', 'ARM']
leds_on = {'IBM': 'A', 'CAR': 'B', 'RAC': 'C', 'LIT': 'D', 'ARM': 'E'}

def query(ip, request):
  host = ip
  port = 9876
  response = 'No connection to server.'
  server = socket.socket()
  try:
    server.connect((host, port))
    server.send(request.encode())
    response = server.recv(4096).decode()
    server.shutdown(socket.SHUT_RDWR)
    server.close()
  except:
    response = 'Error connecting. Is server running/listening on that IP?'
  return response

def decode_leds(code):
  leds = {}
  for led in code:
    if led in '01234':
      leds[leds_available[int(led)]] = 'off'
    else:
      led = int(led, 16) - 10
      leds[leds_available[led]] = 'on'
  return leds

class BombServer:
  ip = '127.0.0.1'
  
  def __init__(self, ip):
    self.ip = ip

  def register(self):
    status = query(self.ip, 'register')
    try:
      status = int(status)
    except:
      status = 'Error getting status. Returned: ' + status
    return status

  def disarm(self):
    status = query(self.ip, 'disarm')
    try:
      status = int(status)
    except:
      status = 'Error getting status. Returned: ' + status
    return status

  def strike(self):
    return query(self.ip, 'add_strike')

  def get_time_remaining(self):
    return query(self.ip, 'time_remaining')

  def get_start_time(self):
    return query(self.ip, 'fuse_start')

  def get_end_time(self):
    return query(self.ip, 'fuse_end')

  def get_status(self):
    status = query(self.ip, 'status')
    try:
      status = int(status)
    except:
      status = 'Error in status. Returned: ' + status
    return status

  def get_bomb(self):
    return json.loads(query(self.ip, 'bomb_object'))

  def get_serial(self):
    return query(self.ip, 'serial')

  def get_leds(self):
    leds = decode_leds(query(self.ip, 'leds'))
    return leds
