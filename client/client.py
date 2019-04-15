import socket
import getopt

class Client:

	def __init__(self, login, password):
		self.__login = login
		self.__password = password
		self.__online = False

	def __repr__(self):
		class_name = type(self).__name__
		return '{}{!r}'.format(class_name, self._login)

	@property
	def get_login(self):
		return self.__login

	@property
	def get_password(self):
		return self.__password

	def set_online(self):
		self.__online = True

	@property
	def get_status(self):
		return self.__online
