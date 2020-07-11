class Tree:
	def __init__(self, data, right=None, left=None):
		self.left = left
		self.right = right
		self.data = data

	def add_leaf(self, leaf, tree):
		if tree:
			if leaf > tree.data:
				if tree.right:
					self.add_leaf(leaf, tree.right)
				else:
					tree.right = Tree(leaf)
			else:
				if tree.left:
					self.add_leaf(leaf, tree.left)
				else:
					tree.left = Tree(leaf)
		else:
			tree = Tree()


	def print_tree(self, tree):
		if tree:
			print(tree.data, end=" ")
			self.print_tree(tree.left)
			self.print_tree(tree.right)

	def find_leaf(self, leaf, tree):
		if tree:
			if leaf == tree.data.login:
				return tree.data
			elif leaf > tree.data.login:
				return self.find_leaf(leaf, tree.right)
			else:
				return self.find_leaf(leaf, tree.left)


if __name__ == "__main__":
	tree = Tree(0)
	tree.add_leaf(15, tree)
	tree.add_leaf(19, tree)
	tree.add_leaf(18, tree)
	tree.add_leaf(0, tree)
	tree.add_leaf(98, tree)
	tree.add_leaf(89, tree)
	tree.add_leaf(89, tree)
	tree.add_leaf(98, tree)
	tree.add_leaf(0, tree)

	tree.print_tree(tree)