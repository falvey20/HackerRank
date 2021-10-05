def fibonacci(n):
    arr = [0, 1]
    for i in range(n+1):
        arr.append(arr[-1]+arr[-2])
    return arr[n]
        

n = int(input())
print(fibonacci(n))
