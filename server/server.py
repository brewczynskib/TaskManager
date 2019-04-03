import socket
import threading
import pickle
import sys
import os
#sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'client'))
sys.path.append(os.path.dirname(sys.path[0]))
from client import client as new_user

_ip = "127.0.0.1"
_port = 5000
_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_server.bind((_ip, _port))
_server.listen(5)

def handle_user(user_socket):
	'''hande user request'''

	receive_data = user_socket.recvfrom(2048)
	#receive file
	user_socket.close()

while True:
	client, addr = _server.accept()
	user_handler = threading.Thread(target = handle_user, args = (client,))
	user_handler.start()
