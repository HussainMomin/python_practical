import array as arr
a = arr.array('i',[2,4,6,8,6,8])

for i in  range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            print(a[j])
      
