file=open("bca.txt","w")
file.write("Hellow my name Hussain Mohammad")
file.close()

file1=open("bca.txt","r")
read = file1.read()
print(read)
vowel_count = 0

for i in read:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='y' or i=='Y' or i=='u' or i=='U':
        vowel_count += 1
print("Number of vowel in string:",vowel_count)