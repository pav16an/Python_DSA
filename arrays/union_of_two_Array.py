def union_array(arr1,arr2):
    a = []
    for i in arr1:
        if i not in a:
            a.append(i)
    for j in arr2:
        if j not in a:
            a.append(j)
    return a
    
arr1 = [1,2,2,3,3,4,5]
arr2 = [1,2,4,5,6,7]
print(union_array(arr1,arr2))
    