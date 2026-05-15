# def linearSearch(n,arr, target): 
#   flag = False
#   for i in range(n):
#     if target != arr[i]:
#       flag = False
#       pass
#     elif target == arr[i] :
#       flag = True
#       loc = i
    
#       # 
    
#     if flag == True:
#       print("Target Found",loc)    
#     else:
#       print("Target not Found") 

def binarySearch(n, arr, target):

    flag = False
    high = n - 1
    low = 0

    while low <= high:

        mid = (low + high) // 2

        if target == arr[mid]:
            flag = True
            loc = mid
            break

        elif target < arr[mid]:
            high = mid - 1

        elif target > arr[mid]:
            low = mid + 1

    if flag == True:
        print("Element Found at index :", loc)
    else:
        print("Element Not Found")


if __name__ == '__main__':

    n = int(input("Enter size : "))

    arr = []

    print("Enter sorted elements:")

    for i in range(n):
        arr.append(int(input()))

    target = int(input("Enter Number Which is to be Search : "))

    binarySearch(n, arr, target)
