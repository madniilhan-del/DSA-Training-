# DSA  : - Data Structures are diffrent ways of organizing data on your computer 
# DSA are store in the format of Stacks and Queues
# ALgo :-  Step by step instruction of any program is called algorithm 
# why are DSA is important  : - library example 

# types of Data Structures 

# Time and Space Complexity 
#   Big O notations : - file ka size increase to notations increase 
#O(N) , O(N2) 
# best case = big omega
# average case = big theta
# worst case  = Big O  (Omicron)
# nested loop = O (n*n)  


a = [5,6,7]
b = [3,6,10]

alice = 0
bob = 0
count = 0 
for i in range(len(a)):
  if a[i] > b[i]:
    alice = alice + 1
    print(alice)
  elif b[i] > a[i]:
      bob = bob + 1 
      print(bob)
  else:
    print(count);    

    
    

 