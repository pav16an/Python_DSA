def remove_dupli(arr):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    print(a)
    
print(remove_dupli([1,2,3,4,4,5,6,7,7,8,8,9,9,9,9]))