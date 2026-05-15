### python contains the following inbuilt type 
import math


# n1 = 4

# print(math.sqrt(n1))
# print(math.pow(n1,2))


a=10 
print(id(a)); 

# all we can use math function  




# n = [10,20,30,40,50]
# print(len(n))

# 2. count() : It returns the number of occurances 
# 3. Insert() and Append() 
# 4. extend
# 5. Remove 
# 6. Pop()
# 7. Reverse() 
# 8. sort() 


# arr = [11,22,33]
# print(arr)
# for i in range(len(arr)):
#   print(arr[i])



# arr = [[1,3,4],22,[4,5]]
# print(arr)
# for x in range (len(arr)):
#   # print(arr[x]) 

#arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr) 

# for i in range (len(arr)):
#   print(arr[i]) ;  # for removing the bracket we use rows and columns 


# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(arr)):
#   for j in range(len(arr[i])):
#     print(arr[i],[j]) 
   










# what is Tuple 

# t=() # this is tuple Syntax
# t1 = tuple() # this is also a Syntax 
# t = (1,2,3,4,5,6)
# print(t)
# print(type(t)) ;

# Set :-  if we want to represent a group of Unique Values 
# s={} # this is Set 
# s = set()
# print(type(s)); 


# # Duplicate Values 
# arr = [1,2,3,4,5,3,2,4,3,2,4,4]
# s = set(arr)
# arr = list(s)
# print(arr) 


# accept the values from the User and print it 

# n = int(input("Enter Size: "))
# print("enter List elemnet : ")
# arr = []
# for i in range(n):
#   ele = int(input("Enter Element : ")) 
#   arr.append(ele)


# for i in range(len(arr)):
#   print(arr[i]);   

# Sum of the Digits of a array of an elements 







# Sum of Even and Odd number : - 
# a = int(input("Enter Size "))
# print("Enter List Elements : ")
# arr=[] 
# even = 0
# odd =  0
# e1 = 0 
# o1 = 0 
# for i in range(a):
#   ele = int(input("Enter Elements")); 
#   arr.append(ele)

# for i in range(len(arr)):
    
#   if(arr[i] % 2 ==0):
#        even = even + arr[i]
#        e1 = e1 + 1 
#   else :
#      odd = odd + arr[i]
#      o1 = o1 + 1   



# print(even)
# print(odd)
# print(e1) ;   
# print(o1); 


       

# TECH Number :- A Number is Called a Tech Number if the given number has an even number of Digits and the number can be divided exactly into two parts from the middle . after equally dividing the number , sum up the number and find the square of the sum 





# 6 digits Tech Number 

# num = int(input("Enter a Tech Number ")) 
# res = 0  
# n1 = num % 1000
# n2 = num // 1000
# res = n1 + n2 
# sq = res * res 

# if(sq == num): 
#  print("given Number is a Tech Number : ",sq) 

# else : 
#  print("Given Number not a Tech Number : ") ; 

# with Loop  

# no = int(input('Enter a Tech Number : ')) ; 
# count = 0 
# save = no 
# while no > 0 : 
#   no = no // 10
#   count = count + 1 
#   no = save 

# if count % 2 == 0:
#   mid = count//2
#   n1= no%10 ** mid
#   n2= no//10 ** mid
#   res= n1 + n2 
#   sq = res * res 

#   if sq == save :
#     print("Tech No"); 
 
#   else: 
#     print("Not Tech Number : ") 




 

