num = int(input("Enter the Number :"))
count = 2

while num!=0:
	for i in range(2,count):
		if count%i==0:
			break
	else:
		print(count)
		num -= 1
	count += 1