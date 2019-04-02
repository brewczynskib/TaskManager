import sys
import socket
import getopt
import pickle
from client import client as new_user

login = ""
password = ""
_host = "127.0.0.1"
_port = 5000
MESSAGE = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(user, message):
	'''send user and message to server'''

	u = pickle.dumps(user)
	m = pickle.dumps(message)

	print('sth',u, m)
	client.send(u)


def sign_in(login, pw):
	'''sign in user'''

	global MESSAGE
	user = new_user.Client(login,pw)
	print('user password', user.get_password())
	MESSAGE = 'sign_in'
	return (user, MESSAGE)


def create_user(login, password):
	'''crate new user nad send to server'''

	global MESSAGE
	user = new_user.Client(login, password)
	MESSAGE = 'create_user'
	send_message(user, MESSAGE)


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
			#create_new_user(args[0], args[1])
			print('type of new user : ', description)
			print('login', args[0], 'password', args[1])
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
