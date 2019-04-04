import sys
import socket
import getopt
import pickle
import json
from client import client as new_user
from serialize_object import convert_to_dict

login = ""
password = ""
_host = "127.0.0.1"
_port = 5000
MESSAGE = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(data, message):
	'''send user and message to server'''
	d = convert_to_dict(data)
	json_data = json.dumps([d,message])
	#m = pickle.dumps(message)
	data_to_send = pickle.dumps(json_data)
	client.send(data_to_send)


def sign_in(login, pw):
	'''sign in user'''

	global MESSAGE
	user = new_user.Client(login,pw)
	print('user password', user.get_password())
	MESSAGE = 'sign_in'
	return (user, MESSAGE)


def create_user(login, password, user_type):
	'''crate new user nad send to server'''

	global MESSAGE
	user = new_user.Client(login, password)
	MESSAGE = 'create_user'
	send_message(user, MESSAGE)
	print('user-type', user_type)


def execute(opts, args):
	'''execute given flags'''

	global login
	global password

	for flag, description in opts:
		if flag in ("-l", "--login"):
			login, password = args
			user, message = sign_in(login, password)
			send_message(user, message)
		elif flag in ("-c", "--create"):
			print('created')
			create_user(args[0], args[1], description)
		elif flag in ("-t", "--tasks"):
			check_tasks(description)
			print('tasks')


def main():

	try:
		client.connect((_host, _port))
	except:
		print('server dont works properly')


	try:
		opts, args = getopt.getopt(sys.argv[1:],"l:c:t"
				 	 ,["login","create","tasks"])
	except:
		print('opsi error')
		manual()

	execute(opts, args)


main()
