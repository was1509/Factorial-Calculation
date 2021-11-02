factorial = 1
n = int(input("Number: "))
constant_n = n
if n == 0:
	print("0! = 1")
else:
	for i in range(n):
		n -= 1
		if n == 0:
			break
		else:
			factorial = factorial * n
	print("{}! = {}".format(constant_n , factorial*constant_n))
