def find_target(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]  + arr[j] == target:
                print(arr[i], arr[j])
                break
    return False
                

arr = [2,4,6,3,2,9]
target = 12
find_target(arr,target)