n = int(input("Enter number : "))
x,y = 0, 1
z = 0

while z<=n:
	print(z)
	x = y
	y = z
	z = x + y
