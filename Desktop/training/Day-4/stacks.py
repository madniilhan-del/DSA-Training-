import sys

class Stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is Pushed")

    def traverse(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack Elements :")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top = self.top - 1
            print(ele, "is Popped")

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top Element :", self.stack[self.top])

    def reverseArray(self, arr):

    # Push all elements
       for i in arr:
        self.push(i)

    rev = []

    # Pop all elements
    while not self.isEmpty():
        rev.append(self.stack[self.top])
        self.pop()

    print("Reversed Array :", rev)        


if __name__ == '__main__':
   
   obj = Stacks()
    # reverse the String using Stacks  
   
    
    
    
    
    
    
    
    
    
    
    
    
    # obj = Stacks()
    # arr = [1,2,3,4,5]
    # rev = []
    # for i in range (len(arr)):
    #     obj.push(arr[i]); 

    # for i in range(len(arr)):
    #     ele = obj.pop ; 
    #     rev.append(ele)
      
    # print(rev)





  
                
 
  
  
#   import sys 
# class Stacks:
#   def __init__(self):
#      self.stack = [] 
#      self.top = -1 
#      self.CAPACITY = 5

#   def isFull(self):
#       if self.top == self.CAPACITY-1:
#          return True 
#       else: 
#          return False 
         

#   def push(self,ele):
#      if self.isFull():
#         print("Stack is Full")
#      else:
#         self.top = self.top + 1 
#         self.stack.append(ele)
#         print(ele,"is Pushed")      

#   def traverse(self):
#      for i in range(self.top,-1,-1):
#         print(self.stack[i]) 


#   def isEmpty(self):
#      if self.top == -1 :
#          return True
#      else:
#         return False 
         

#   def pop(self):
#     if (self).isEmpty():
#        print("Stack is Empty ") 
#     else : 
#        ele = self.stack[self.top]
#        self.stack.pop()
#        self.top = -1
#     return ele      

#   def peek (self):
#     print() 
  
#   def exit(self):
#      pass
 



# if __name__ == '__main__':
#   obj = Stacks()
#   while True:
#     print("1 . Push")
#     print("2 . Pop")
#     print("3 . Peek")
#     print("4 . Traverse")
#     print("0 . Exit")  
#     ch = int(input("Select Any Choice "))
#     if ch == 1:
#         ele = int(input("Enter Data : "))
#         obj.push(ele)
#     elif ch == 2 :
#        obj.pop()

#     elif ch == 3:
#        obj.peek()

#     elif ch == 4:
#       obj.traverse

#     elif ch == 0 :
#        sys.exit(0); 
         
                
 
  
  
  
  
  
  
  
  
  










