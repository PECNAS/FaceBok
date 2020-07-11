from coding import encoding

class Client:
	def __init__(self, login, psswd):
		self.login = login
		self.psswd = encoding(psswd)

	def __str__(self):
		return self.login

	def __gt__(self, obj):
		return self.login > obj.login

	def __eq__(self, obj):
		return self.login == obj.login


	def check_psswd(self, psswd):
		return self.psswd == encoding(psswd)

	def get_name(self):
		return self.login

	def to_login(self):
		print(f"Клиент {self.login} вошёл")

if __name__ == "__main__":
	c1 = Client(12, "11032004")
	c2 = Client(2, "11032004")
	print(c1 == c2)
	print(c1 > c2)
	print(c1 < c2)
	print()
	print()
	print()