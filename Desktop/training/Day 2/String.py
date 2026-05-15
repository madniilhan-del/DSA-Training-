# #find() :- returns and index number ,, scans the character from left to right 

# s="Learning Python is very easy from Ashish Sir"
# print(s.find('Python'))#9
# print(s.find("Java")) #-1
# print(s.find("r")) #3
# print(s.rfind("r")) #43

# ## Counting the Substring 
# s="abcabcabcabcadda"
# print(s.count('a')); 
# print(s.count('ab')); 
# print(s.count('a',3,10))

# # replace function  old string to New String 
# r="Learning Python is very difficult easy from Ashish Sir"
# # s2 = r.replace("difficult","easy")
# # print(s2); 
# ls = r.split()
# print(ls)
# print(len(ls))

# a = "22-02-2022"
# l = s.split("-")
# print(l) 


# t = ['Nagpur','Pune','Mumbai','Delhi']
# s = ' '.join(l)
# print(s)



# input = "Learning Python is very difficult easy from Ashish Sir"
# inp = input.split() ;
# rev = inp[::-1]
# print(rev) 
 




# Q3 Program to reeverse internal content of each word

# input = "Learning Python is Very Easy from Ashish Sir" 

# inp = input.split(); 
# ans = " "
# print(inp)
# for i in range (len(inp)):
#    ans = ans + inp[i][::-1] + " "
# print(ans)


# Q4 Write a Program to remove Duplicate Characthers from the given input String 
# input = "ABCDABBCDABBBCCCDDEEEF" ; 
# out = ""


# for i in range (len(input)):
#   if input[i] not in out :
  
#    out = out + input[i]

# print(out);   


# Q Accept mobile Number check that mobile number is 10 digit only and  digit only  .. Check number is valid in india or not (6,7,8,9) 



num = input("enter a 10 digit Number "); 

if num.isdigit():
  if len(num)== 10:
    print("Valid Number : " ,num)
    if num.startswith(6) or num.startswith(7) or num.startswith(8) or num.startswith(9):
      print("Valid Number : ",num )   
  else:
    print("Not a valid Number : " ,num)
  










