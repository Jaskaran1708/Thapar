arr = [55, 21, 77, 45, 96];    
max = arr[0];
for i in range(0, len(arr)):    
   if(arr[i] > max):    
       max = arr[i];    
print("Largest element present in given array: " + str(max));   