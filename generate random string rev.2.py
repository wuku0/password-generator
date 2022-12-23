import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIFKLMNOPQRSTUVWXYZ123456!@#$%^&*()_+={}[]\|:;/?.,><|`~*-"

while 1:
	password_len = int(input("How many characters should the password be : "))
	password_count = int(input("How many passwords should be generated : "))
	for x in range(0,password_count):
		password = ""
		for x in range(0,password_len):
			password_char = random.choice(chars)
			password = password + password_char	
		print("Here is your password : ", password)	
