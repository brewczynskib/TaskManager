import socket
import threading
import pickle
import sys
import os
import json
#sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'client'))
sys.path.append(os.path.dirname(sys.path[0]))
from client import client as new_user
from serialize_object import object_to_dict

_ip = "127.0.0.1"
_port = 5000
_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_server.bind((_ip, _port))
_server.listen(5)

def handle_user(user_socket):
	'''handle user request'''

	receive_data, addr = user_socket.recvfrom(1024)
	json_file = pickle.loads(receive_data)
	d, message = json.loads(json_file)
	data = new_user.Client(d['login'], d['password'])
	print('data', ':', data.get_login())
	print('message: ', message)
	user_socket.close()

while True:
	client, addr = _server.accept()
	user_handler = threading.Thread(target = handle_user, args = (client,))
	user_handler.start()
