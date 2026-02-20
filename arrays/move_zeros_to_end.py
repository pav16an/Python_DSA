#using Broute force 
def move_zero(arr):
    arr1 = []
    for num in arr:
        if num == 0:
            arr1.append(num)
            arr.remove(num)
    arr.extend(arr1)
    print(arr)
#using optimal way
def moveZeros(arr):
    j=0
    for i in range(len(arr)):
         if arr[i]!=0:
             arr[j] = arr[i]
             j+=1
    while(j < len(arr)):
        arr[j] = 0
        j+=1
    
    print(arr)
arr = [0,1,3,0,2,6,0,3,0,6]
moveZeros(arr)
    