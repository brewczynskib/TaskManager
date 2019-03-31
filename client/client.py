import socket
import getopt

class Client:

	def __init__(self, login, password):
		self._login = login
		self._password = password

	def get_login(self):
		return self._login

	def get_password(self):
		return self._password
