import sys
import socket
import getopt
import pickle
import Client
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
	'''sign_in user'''

	global MESSAGE
	user = us.Client(login,pw)
	MESSAGE = 'sign_in'
	return (user, MESSAGE)


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
		elif flag in ("-t", "--tasks"):
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
