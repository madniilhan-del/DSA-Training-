# num = int(input('Enter a number'))
# res = num % 10 ;

# print(res); 
 
# print('the last digit of a number :- ',res)  #### 10)120( 12   % it always gives the remainder  

#sum of two digit number 

# num  = int(input('Enter Your Number : '))
# n1 = num % 10; 
# n2 = num // 10 ; 

# res = n1 + n2

# print(res); 





##  sum of 3 digit number 
# num = int(input('Enter a 3 digit number = '))
# n1 = num % 10 ; #3
# num = num // 10 #12
# n3 = num % 10 #2 
# num = num // 10 #1


# res = n1 + num + n3 
# print(res)





# num = int(input('Enter a 5 digit number = '))
# n1 = num % 10  # 6 
# num = num // 10  # 45 
# n2 = num % 10  # 5 
# num = num // 10 # 4 

# n3 = num % 10 ; 
# num = num // 10 

# n4 = num % 10 
# num = num // 10 

# n5 = num % 10 

# res  = n1 + n2 + n3 + n4 + n5 
# print(res)


## Enter a number in reverse 

# num = int(input('Enter a number') ); 

# n1 = num % 10 ; 
# num = num // 10 
# n2 = num % 10 ; 
# num = num // 10 
# n3 = num % 10 

# res  = n1 * 100 + n2 * 10 + n3 * 1 ; 

# print (res);  



# ###  
# num = int (input('Enter a number = ')) 
# n1 = num % 10 # 9 
# n2  = num // 1000000000


## reverse the number 

# num = int(input('Enter a Number'))
# rev = 0 

# while num > 0:
#   rem = num % 10 
#   rev = rev * 10 + rem
#   num = num // 10 


# print(rev)
# Count the Digits no = 123456 


# num = int(input('Enter the Digits'))
# count = 0 

# while num > 0 :
#   num = num // 10 
#   count = count + 1

# print(count)  




# print( 'number Counts :- ',count) ;  \


# sum of the digits  ==  456 = 4 + 5 + 6 == 


# num= int(input('Enter your number  :- ')) ; 
# sum = 0

# while num > 0 : 
#   num = num % 10 
#   sum = sum + num 
#   num = num // 10 
  
#   print(sum)


# num = int(input('Enter a number '))  
# sum = 0 

# while num > 0 :
#   rem = num % 10 
#   sum = sum + rem
#   rem = num // 10  

# print(sum)
 


## factorial of a number  
num = int (input("Enter a Number : ")) 

fact = 1
# for i in range(1,num+1):
#   fact = fact * i
# print(fact)  

i = 1
while i < num + 1:
  fact = fact * i 

  i = i + 1 

print(fact)







## palindrome 

# num = int(input('Enter a number')); 
# rem = 0 
# save = num 
# while num > 0 :

#   rem = num % 10 
#   rev = rev * 10 + rem 
#   num = num // 10 

#   if(rev == save):
#     print('no. is a palindrome ') 
#   else : 
#     print('not a palindrome ') ; 








 # peterson number :- a number is said to be peterson if the sum of the factorials of each digits is equal to sum of the number itself 
 # number = 145 
 # 145 = !1 + !4 + !5 
# = 1 + 24 + 120  = 145 and 145 is a peterson number 


no = int (input('Enter a number : '))

sum = 0 

save = no 
 

while no > 0 :
  rem = no % 10 ; 
  fact = 1
  while rem > 0:  
   fact = fact * rem 
   rem = rem - 1  
   sum = sum + fact 
   no = no//10 

  if save == sum :
     print('number is a peterson number : ',save)
  else:
    print('number is not a peterson number')

      


 
 
