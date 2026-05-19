# insert elemant in an array 
# arr= []
# n = int(input("Enter Size of an array ")) 
# for i in range (n):
#       arr.append(int(input("Enter Element")))
# key = int(input("Enter key which is to be Insert : "))

# loc = int(input("Enter Location "))  
  
# arr.append(0)


   
  
# for i in range(len(arr)-1 , loc, -1) :
#       arr[i] = arr[i-1] 
# arr[loc] = key 
# print(arr)    \

# arr= []
# n = int(input("Enter Size of an array ")) 
# for i in range (n):
#       arr.append(int(input("Enter Element")))


# loc = int(input("Enter Location "))  
  
# #arr.append(0)

# for i in range (loc+1,len(arr)):
#       arr[i-1] = arr[i]
#       arr.pop()

# print(arr);      




# array rotation 
# Question : Rotatate an array to the right by a given number of steps 
# sample input:[1,2,3,4,5]
# Expected Output : [4, 5, 1 , 2 , 3 ] 

# arr = []
# n = int (input("Enter size of an array "))  
# for i in range(n):
#       arr.append(int(input("Enter an Element :"))) 

# arr = [1,2,3,4,5]
# k= 2
# for i in range(k):
#     for i in range(len(arr)-1, 0, -1):
#       temp = arr[i] 
#       arr[i]= [arr[i-1]] 
#     arr[0] = temp 
# print(arr)


#Intersection of two Arrays:
# Question : Find the intersection of two arrays . 
# Sample input : [1,2,2,1] and [2,2]
# Expected Output :[2]

arr = [1,2,2,1]
arr1 = [2,2]
result = []
for i in range(len(arr)):
   if i in arr1 and i not in result:
      result.append(i)

print(result)      


# question Given an array containing both Positive and negative numbers , rearrange them in an alternating fashion 

# logic : Seperate positive and negative 




# Reeverse a string without inbuild function and shortcut 

#Q : Write  a program to reverse a given String .
# Sample Input :"Hello"
# Expected Output : "olleH"
r = "Hello"
rev=""
for i in range (len(r)-1,-1 , -1) :
 
    rev = rev + r[i] 
  
print(rev)


# Check for a valid palindromic string : 
# Question ; Write a program to check if a given 
     
s = "A man , a plan , a canal: Panama"
str = ""

for i in range (len(s)):
    st = s[i].lower()
    if st.isalpha():
       str = str + st

    rev = str[::-1]
 
    
if rev == str:
       print("palindrome")
else:
       print("not palindrome ")      

    

# Check for anagrams to check if two strings are anagrams of each other 
#logic : Check if the character counts in both Strings are the same .
#sample Input : "Listen" and "Silent"
#Expected Output : anagrams 

st1 = ""
st2 = "" 

s1 = st1.lower()
s2 = st2.lower()

for i in range(len(s1)):
     if sorted(s1) == sorted(s2):
          print("anagrams string")

     else:
          print("not anagrams")  



    

















