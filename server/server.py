import socket
import threading
import pickle
import sys
import os
import json
import sqlite3
#sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'client'))
sys.path.append(os.path.dirname(sys.path[0]))
from client import client as new_user

_ip = "127.0.0.1"
_port = 5000
_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

_server.bind((_ip, _port))
_server.listen(5)


def is_user_in_db(login):
	'''check if user is in db'''

	return True

def enter_user(login, password, user_socket):
	'''check if user is in db if is, user can log-in'''

	if is_user_in_db(login,password):
		response = new_user.Client(login, password)
		user_socket.send(pickle.dumps(response))
		print('data sent to client')

	else: pass


def create_user(login, password, user_socket):
	'''create new user'''

	data = (login, password)
	login = (login,)
	conn = sqlite3.connect("example.db")
	c = conn.cursor()
	c.execute("CREATE TABLE users (login text, password text)")

	print(login)
	if(c.execute("SELECT * FROM users WHERE login = ?", login)):
		c.execute("INSERT INTO users VALUES (?,?)", data)
		conn.commit()
		user_socket.send(b'Account created')
	else:
		user_socket.send(b'Login alredy used in the data base')
		print('login already used in db')
	conn.close()
def handle_user(user_socket):
	'''handle user request'''

	receive_data, addr = user_socket.recvfrom(1024)
	data = pickle.loads(receive_data)
	message = data['message']
	print('data ', data)

	if message in ("-l" , "--login"):
		enter_user(data['login'], data['password'], user_socket)
		print('login')
	elif message in ("-c", "--create"):
		create_user(data['login'], data['password'], user_socket)
		print('create')

	user_socket.close()

while True:

	client, addr = _server.accept()
	user_handler = threading.Thread(target = handle_user, args = (client,))
	user_handler.start()
