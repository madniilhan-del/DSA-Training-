# def add():
#   a = int(input("Enter a : "))
#   b =int (input("Enter b : " ))
#   res= a + b 
#   print("Addition is : ",res)


# if __name__ == '__main__':
#   add()
  
# function with Parameters 

# def add(a,b):

#  res = a + b 
#  print("Adddition of a two number is  : " ,res)


# if __name__ == '__main__':
#  a = int(input("Enter number a"))
#  b = int(input("Enter number b")) 
#  add(a,b); 


#function with return values with parameters 

# def add(a,b):
#   res = a + b 
#   return res


# if __name__ == '__main__':
#   a = int(input('Enter A '))
#   b = int(input('Enter B '))
#   r = add(a,b) 
#   print("Addition is ",r)

    
# We can return multiple values in python because pyhton is a strong Language 

def add(a, b):
  
  res1  =  a + b 
  res2  =  a - b
  res3  =  a * b 

  return res1,res2,res3
 

if __name__ == '__main__':
 a = int(input('Enter A '))
 b = int(input('Enter B '))
 r1 , r2 , r3 = add(a,b) 
 print("Addition is ",r1)  
 print("Subtraction is ",r2)  
 print("multiplication is ",r3) 

 



