def maxSum(arr, n, k):
    if (n < k):
        print("Invalid")
    else:
       sum = 0
       for i in range(k):
          sum = sum + arr[i]
       curr_sum = sum
       for i in range(k, n):
          curr_sum = curr_sum + arr[i] - arr[i-k]
          sum = max(sum, curr_sum)
       return sum
arr = [1,2,3,4,5,6,7,8]
k = 4
n = len(arr)
print(maxSum(arr, n, k))