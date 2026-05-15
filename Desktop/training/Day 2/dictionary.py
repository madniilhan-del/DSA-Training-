# d = {}
# d[100] = "Ashish" 
# d[200] = "Ilhan"
# d[300] = "sandeep"

# print(d)

rec = {} 
n = int (input("Enter Number of students : "))
for i in range(n):
  name = input("Enter Name : ")
  per = float(input("Enter Perc : "))
  rec[name] = per


print(rec)
for x in rec:
  print(x,"\t",rec[x])




d = {100:'Ilhan',200:''}  
