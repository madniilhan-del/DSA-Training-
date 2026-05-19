#Amazon 
#3. Edit Distance 
# Given two strings 
# s = "ycce" and t = " ycse "
# output : 1
# Explanation : One operation is required 
# inserting 's' between two 'e' of s .
# example 2 :
# Input:
#s = "h4c" , t ="h4c"
# Output:
# 0 
# Explanation : Both Strings are same 
# 

s ="ycce"
t ="yctce"
output = 0 
count  = 0 

if len(s) < len(t):
  output = len(t) -len(s)
elif len(t) < len(s):
  output = len(s) - len(t)

elif len(s) == len(t):
  for i in range(len(s)):
    if s[i] != t[i]:
      count = count+1

  output = count
print(output);  










