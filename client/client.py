import socket
import getopt

class Client:

	def __init__(self, login, password):
		self._login = login
		self._password = password
		self._online = False

	def __repr__(self):
		class_name = type(self).__name__
		return '{}{!r}'.format(class_name, self._login)

	def get_login(self):
		return self._login

	def get_password(self):
		return self._password

	def set_online(self):
		self._online = True

	def get_status(self):
		return self._online
