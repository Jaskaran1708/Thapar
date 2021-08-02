def segregateElements(arr, n):
    temp = [0 for k in range(n)]
    j = 0 
    for i in range(n): 
        if (arr[i] >= 0 ): 
            temp[j] = arr[i] 
            j = j + 1
    if (j == n or j == 0): 
        return 
    for i in range(n): 
        if (arr[i] < 0): 
            temp[j] = arr[i] 
            j = j + 1
    for k in range(n): 
        arr[k] = temp[k]
arr = [3,4,-5,9,-23,56,-98,-34,1] 
n = len(arr)
segregateElements(arr, n);
for i in range(n): 
    print(arr[i]) 