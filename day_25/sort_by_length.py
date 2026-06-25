names = ['Rahul','Aman','Ansh','Deepak']
for i in range(0,len(names)-1):
    for j in range(0,len(names)-1-i):
        if len(names[j])>len(names[j+1]):
            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp
print(names)            