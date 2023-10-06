from random import randint, choice
import string
def pwd(length):
	
	
	
	password = ""
	sp = ['!',"@","#","$","%","^","&","*","?","."]
	for i in range(1,length):
		rndm = randint(-2,9)
		if rndm<0:
			password+=choice(sp)
		elif rndm % i == 0:
			password+=choice(string.ascii_letters)
		else:
			password+=choice(string.digits)
	return password

row = int(input("length for password: "))
print(pwd(row))