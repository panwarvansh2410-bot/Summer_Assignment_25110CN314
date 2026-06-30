str1 = 'Must Watch Sapne Vs Everyone'

def length(str1):
    count = 0
    for i in range(0,len(str1)):
        if str1[i]!=" ":
            count+=1
    return count  

def reverse(str1):
    n = len(str1)
    temp =""
    for i in range(0,n):
        temp = temp + (str1[n-1-i])
    return temp

def cons(str1): 
    vow = ['A','E','I','O','U','a','e','i','o','u']
    count = 0
    n = len(str1)
    for i in range(0,n):
        if str1[i] not in vow:
            count+=1
    return count

def vow(str1): 
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    count = 0
    n = len(str1)
    for i in range(0,n):
        if str1[i]  in vowel:
            count+=1
    return count                          

def word(str1):
    n = len(str1)
    count = 1 
    for i in range(0,n):
        if str1[i]==" ":
            count+=1
    return count

def palind(str1): 
    n = len(str1)
    flag = 0
    for i in range(0,n):
    
        if str1[n-1-i] == str1[i]:
            flag = 1
        else:
            flag = 0
            break

    if flag == 1:
        print("Yes",str1,"is Palindrome")
    else:
        print("NO",str1,"is not Palindrome") 

def rotate(str1):
    n = len(str1)
    k = int(input("enter key that has to rotate string :"))
    temp =""
    for i in range(k,n):
        temp+=(str1[i])
    for j in range(0,k):
        temp+=(str1[j])

    return temp       








while True:

    print("\n Menu Driven String Operation ")
    
    print("1. length of string ")
    print("2. Reverse String ")
    print("3. Count vowels ")
    print("4. count consonant ")
    print("5. count words ")
    print("6. palindrome checking ")
    print("7. String rotation ")
    print("8. Exit the Array operator ")
    choice = input("Enter your choice : ")

    

    match choice:
            case '1':
                
                print("Result =", length(str1))


            case '2':
              print("Result =", reverse(str1))

            case '3':
                
                print("Result =", vow(str1))
                    
            case '4':
                print("Result =", cons(str1))

            case '5': 
                print("Result =", word(str1))

            case '6': 
                print("Result =", palind(str1))

            case '7': 
                print("Result =", rotate(str1))
    
            case '8':
                break

            case _:
                print("Invalid choice")