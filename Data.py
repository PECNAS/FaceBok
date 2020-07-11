from Client import Client

class Data:
	clients_val = 0

	def add_new_client(self, login, psswd, tree):
		client = Client(login, psswd)
		tree.add_leaf(client, tree)
		self.clients_val += 1


	def find_client(self, login, tree):
		return tree.find_leaf(login, tree)

	def get_number_of_clients(self):
		return self.clients_val