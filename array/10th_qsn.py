def RangeAndCoef(arr, n):
    max = getMax(arr, n)
    min = getMin(arr, n)
    range = max - min
    coef = range / (max + min)
    print("Range :", range)
    print("Coefficient of Range :", coef)
def getMax(arr, n):
    a = arr[0]
    for i in range(1, n):
        a = max(a, arr[i])
    return a
def getMin(arr, n):
    a = arr[0]
    for i in range(1, n):
        a = min(a, arr[i])
    return a    
if __name__ == '__main__':
    arr = [4,10,3,54,5]
    n = len(arr)
    RangeAndCoef(arr, n)