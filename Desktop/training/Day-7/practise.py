
arr =[12, 35, 1, 10, 34, 1] 
        
def getSecondLargest(arr):
        arr.sort() 
        largest = arr[-1]
        print(largest)

        for i in range(len(arr)-2,-1,-1):
               print(arr[i])
               if arr[i] != largest:
                   print(arr[i])
                   return arr[i]     
                
    
        return -1              

        

       
          
                  
print(getSecondLargest(arr));
      
      
      



        