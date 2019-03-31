import socket
import threading
import pickle


_ip = "127.0.0.1"
_port = 5000
_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_server.bind((_ip, _port))
_server.listen(5)

def handle_user(user_socket):
	'''hande user request'''

	user, message = user_socket.recvfrom(2048)
	if(not user): print('uopsi')
	user = pickle.loads(user)
	print(message)
	user_socket.close()

while True:
	client, addr = _server.accept()
	user_handler = threading.Thread(target = handle_user, args = (client,))
	user_handler.start()


