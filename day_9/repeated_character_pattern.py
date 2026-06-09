char_list = ['A','B','C','D','E']
for i in range(0,len(char_list)):
    for j in range(0,i+1):
        print(char_list[i],end=" ")

    print()