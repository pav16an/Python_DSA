arr = [20,8,6,3,99,55,4]
sort = sorted(arr)
print(sort)
k = 2
for i in range(len(sort)):
    if i == k:
        print(sort[i])
