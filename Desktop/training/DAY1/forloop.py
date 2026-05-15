# for x in range(10):
#   print(x)




# for i in range(1,11,2):
#   print (i)


#   # reverse 

# for i in range(10,0,-1):
#   print(i) 


# arr = [1,2,3,4,5,6]
# for i in range (len(arr)):
#   print(arr[i])


# for x in arr:
#   print(x)


# i = 1 
# j = 10
# while i<j :
#   print(i,"\t",j)

#   i = i + 1
#   j = j - 1




# ls = []
# print(type(ls))

# ls = list()
# print(type(ls))

# how to traverse or print a list 
# print(arr)

# for i in range(len(arr)):
#   print(arr[i])


# for i in range(len(arr)):
#   print(arr[i],end= " ")

# print()


# for x in arr:
#   print(x,end=" ")

#slicing of array
# arr = [1,2,3,4,5,6,7,88,99]
# print(arr[1:5])
# print(arr[4:6])
# print(arr[:6])
# print(arr[4:])
# print(arr[:])
# print(arr[::1])
# print(arr[::2])
# print(arr[::3])
# print(arr[::-1])
# print(arr[::-2])


# find the maximum and minimum Elements : 
#Question : Write a function to find the maximum and minimum 
# elements in an array 
# sample Input : [5,3,9,2,8]
# expected Output : Maximum : 9 , Minimum: 2 

# arr = [5,3,9,2,8]
# max = arr[0] 
# min = arr[0]
# for i in range (1,len(arr)):
#   if max<arr[i]:
#     max=arr[i]
    
#   elif min > arr[i]:
#     min = arr[i]
   



 

# print(max)
# print(min) 

 # in  and not In operator for finding duplicates in an unsorted array

#ans=[]
# ans.append(arr[i])


# Remove Duplicates from Unsorted Array : 
# Sample Input : [3,2,3,1,2,4]
# expected output : [3,2,1,4]
arr = [3, 2, 3, 1, 2, 4]

ans = []

for i in arr:
    if i not in ans:
        ans.append(i)

print(ans)