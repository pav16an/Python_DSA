def Remove_duplicate(arr):
    arr1 = []
    for i in range(len(arr)):
        if arr[i] not in arr1:
            arr1.append(arr[i])
    return arr1


def check_duplicate(arr):
    return len(arr)!= len(set(arr))


def check_duplicate2(arr):
    arr1 = []
    for i in range(len(arr)):
        if arr[i] not in arr1:
            arr1.append(arr[i])
    if len(arr1) != len(arr):
        return True
    else:
        return False
arr = [1, 2, 3, 4, 5, 1, 2, 3]
print(Remove_duplicate(arr))
arr = [1, 2, 3, 4, 5, 1, 2, 3]
print(check_duplicate(arr))
arr = [1, 2, 3, 4, 5, 1, 2, 3]
print(check_duplicate2(arr))



