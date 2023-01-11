no = int(input("Enter the number : "))
total = 0
while(no>0):
	temp = no%10
	total = total+temp
	no = no//10
	print("Sum of digits =",total)