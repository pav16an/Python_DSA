def linear(arr,n):
    for i in range(len(arr)):
        if n == arr[i]:
            print(f"{n} is located at index {i}")

arr = [12,35,5,36,3]
n = 36
linear(arr,n)