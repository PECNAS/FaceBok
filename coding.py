import hashlib

def encoding(psswd):
	h = hashlib.md5(bytes(psswd.encode()))
	p = h.hexdigest()

	return p

if __name__ == "__main__":
	print(encoding("Привет"))