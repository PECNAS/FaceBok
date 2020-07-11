import time
from Client import Client
from Data import Data
from myTree import Tree

start = time.time()

FILE = "requests.txt"

if __name__ == "__main__":
	data = Data()
	tree = Tree(Client("AAA", "AAA"))

	with open(FILE, 'r') as file:
		n = int(file.readline())
		for i in range(n):
			nickname, psswd = file.readline().strip().split()
			client = data.find_client(nickname, tree)
			if client:
				is_psswd = client.check_psswd(psswd)
				if is_psswd:
					client.to_login()
			else:
				data.add_new_client(nickname, psswd, tree)
			

	print(f"Clients quantity: {data.get_number_of_clients()}")
	print(time.time() - start)