def find_duplicates(arr):
    freq = {}
    for num in arr:
        if num not in freq:
           freq[num] = 1
        else:
            freq[num] += 1
    for i in freq:
        if freq[i] > 1:
            print(f"{i} occurs {freq[i]} times")
arr1 = [1,2,3,2,5,2,3]
find_duplicates(arr1)