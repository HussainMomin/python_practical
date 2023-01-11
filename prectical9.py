Number = int(input("Enter the Number:"))
fact = 1
for i in range(1,Number+1,1):
    print(i)
    fact = fact*i
print("Factorial is =",fact)