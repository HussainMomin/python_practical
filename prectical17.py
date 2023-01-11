my_list = []
my_list=['A','B','C','D']

print("First Element: ",my_list[0])
print("Last Element: ",my_list[-1])

print("Element 1st index to 2nd index",my_list[1:3])

 
my_list.append('E')
print(my_list)

my_list.insert(2,'c')
print(my_list)

my_list.extend(my_list)
print(my_list)

my_list.remove('A')
print(my_list)