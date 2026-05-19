arr= [1,2,3]
n  = len(arr)
ans = [0] * 2* n
for i in range(n):
  ans[i] = arr[i]
  ans[i+n] = arr[i]

print(ans)
