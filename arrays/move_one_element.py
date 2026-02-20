def move_to_end(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    print(arr)
        
        

move_to_end([1,2,3,4,5,6,7,8,9])