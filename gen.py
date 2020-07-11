import random

FILE = "requests.txt"
MAX_LOGIN_NUMBER = 100
REQUESTS_QUANTITY = 1000000
PASSWORD_LEN = 8
NAMES = [
			"Albert","Alejandro","Alex","Alexander","Alfred",
			"Angelina","Anita","Ann","Ariana","Arianna",
			"Ashley","Audrey","Autumn","Ava","Avery",
			"Benjamin","Bernard","Blake","Brandon",
			"Brian","Bruce","Bryan","Bailey","Barbara","Beatrice",
			"Carl","Carlos","Charles","Christopher","Cole",
			"Clifford","Cody","Colin","Curtis","Cyrus","Caroline",
			"Claire","Daniel","David","Dennis","Devin","Diego",
			"Deborah","Delia","Destiny","Diana","Dorothy",
			"Francis","Fred","Faith","Fiona","Florence","Freda",
			"Gabriel","Gavin","Geoffrey","George","Gerld","Gilbert",
			"Gordon","Graham","Gregory","Gloria","Gabriella",
			"Isaiah","Isabel","Isabella","Jack","Jackson","Jacob","Jaden",
			"Jake","James","Jason","Jayden","Jeffery","Jeremiah","Jesse",
			"Jesus","John","Jonathan","Jordan","Jose","Joseph","Joshua",
			"Juan","Julian","Justin","Jacqueline","Jada","Jane","Jasmine",
			"Jenna","Jennifer","Jessica","Jocelyn","Jordan","Josephine",
			"Joyce","Julia","Keith","Kevin","Kyle","Kaitlyn","Katelyn",
			"Landon","Lawrence","Leonars","Lewis","Logan","Louis",
			"Leslie","Lillian","Lily","Linda","Lorna","Luccile","Lucy",
			"Lynn","Malcolm","Martin","Mason","Matthew","Michael","Miguel",
			"Miles","Morgan","Mabel","Mackenzie","Madeline","Madison",
			"Maya","Megan","Melanie","Melissa","Mia","Michelle",
			"Mildred","Molly","Monica","Nathan","Nathaniel","Neil",
			"Patrick","Peter","Philip","Paige","Pamela","Patricia",
			"Pauline","Penelope","Priscilla","Ralph","Raymond",
			"Reginald","Richard","Robert","Rodrigo","Roger",
			"Sarah","Savannah","Sharon","Sheila","Shirley",
			"Sierra","Sofia","Sophia","Stephanie","Susan"
		]

def get_random_password():
	psswd = ''
	for i in range(PASSWORD_LEN):
		psswd += chr(random.randint(33, 126))
	return psswd


with open(FILE, 'w') as file:
	file.write(str(REQUESTS_QUANTITY) + '\n')
	for _ in range(REQUESTS_QUANTITY):
		line = random.choice(NAMES) + '_' + str(random.randint(1, MAX_LOGIN_NUMBER))
		line += ' ' + get_random_password() + '\n'
		file.write(line)