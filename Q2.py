
def minChar(n, password):
	spec = ["!", "@", "#", "$", "%"]
	count = [0, 0, 0, 0]
	for i in password:
		if i in spec:
			count[0] += 1
		elif i.isdigit():
			count[1] += 1
		elif i.isupper():
			count[2] += 1
		elif i.islower():
			count[3] += 1
	print("Password contains\nSpecial Characters =", count[0], "\nDigits =", count[1], "\nUppercase Alphabets =", count[2], "\nLowercase Alphabets=", count[3]);
	if(n >= 8):
		if 0 not in count:
			print("Strong password good to go!")
	else:
		print(8-n, "more Characters required")

n = int(input())
password = input();
minChar(n, password)

