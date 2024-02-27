def PairsCount(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count = count + 1
    return count
arr = [3,5,4,6,7,2,5,7]
n = len(arr)
sum = 9
print("Number of pairs are: ",
      PairsCount(arr, n, sum))