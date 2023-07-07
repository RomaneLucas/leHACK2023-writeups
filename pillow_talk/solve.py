import socket
import itertools

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',8000))
s.recv(1024)

_preamble = 'AAAAAAAA'.encode('utf-8')
_syncword = '27ABFF3D'.encode('utf-8')
_header = 'BF67'.encode('utf-8')

j = '0123456789ABCDEF'
y = ''
for i in itertools.product(j,repeat=2):
  _payload = (y+''.join(i)).encode('utf-8')
  s.send(_preamble+_syncword+_header+_payload)
  data = s.recv(1024)
  if 'leHACK{' in data.decode('utf-8'):
    print(data)
    break
