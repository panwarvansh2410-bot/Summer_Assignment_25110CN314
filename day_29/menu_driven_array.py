arr = [9,5,7,43,56,12,3,1,2]

def insert(arr):
    k = int(input("enter your number :"))
    arr.append(k)
    return arr

def delete(arr):
    k = int(input("Enter element to delete: "))
    if k in arr:
        arr.remove(k)
    else:
        print("Element not found")
    return arr

def search(arr):
    a = int(input("enter the element to be search :"))
    for i in range(0,len(arr)):
        if arr[i]==a:
            print("Element is Found!!")
            return
    print('element not found')

def display(arr):
    
    return arr

def maxm(arr):
    large = arr[0]
    for i in range(0,len(arr)):
        if arr[i]>large:
            large = arr[i]
    return large

def minm(arr):
    small = arr[0]
    for i in range(0,len(arr)):
        if arr[i]<small:
            small = arr[i]
    return small

def sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr






while True:

    print("\n Menu Driven Array Operation ")
    
    print("1. Insert the element ")
    print("2. Delete element ")
    print("3. Search the element ")
    print("4. Display array ")
    print("5. Find Maximum ")
    print("6. Find Minimum ")
    print("7. Sort the Array ")
    print("8. Exit the Array operator ")
    choice = input("Enter your choice : ")

    

    match choice:
            case '1':
                
                print("Result =", insert(arr))


            case '2':
              print("Result =", delete(arr))

            case '3':
                
                print("Result =", search(arr))
                    
            case '4':
                print("Result =", display(arr))

            case '5': 
                print("Result =", maxm(arr))

            case '6': 
                print("Result =", minm(arr))

            case '7': 
                print("Result =", sort(arr))
    
            case '8':
                break

            case _:
                print("Invalid choice")