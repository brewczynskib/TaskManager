import sys
import socket
import getopt
import pickle
#from client import client as new_user
#from serialize_object import convert_to_dict

login = ""
password = ""
_host = "127.0.0.1"
_port = 5000
message = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(data, message):
	'''send user and message to server'''

	_data = {"login": data[0] , "password": data[1], "message": message}
	data_to_send = pickle.dumps(_data)
	print('bytes sent: ', client.send(data_to_send))


def handle_user(login, password, flag):
	'''create or login user'''

	global message
	message = flag
	data = [login, password]
	send_message(data, message)
	print('make some action', flag)
	while True:
		self = client.recv(1024)
		self = pickle.loads(self)
		if(self):
			self.set_status()
			print('loged in ', self.get_login() , 'online :', self.get_status)
			break


def execute(opts, args):
	'''execute given flags'''

	global login
	global password

	for flag, description in opts:
		if flag in ("-l", "--login"):
			print('login')
			handle_user(args[0], args[1],flag)

		elif flag in ("-c", "--create"):
			print('created')
			handle_user(args[0], args[1],flag)

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
