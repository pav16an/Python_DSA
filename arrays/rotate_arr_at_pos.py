def rotate(k,arr):
  arr1 = []
  for i in range(k,len(arr)):
    arr1.append(arr[i])
  for i in range(k):
    arr1.append(arr[i])
  return arr1
  
def rotate2(arr, k):
    k = k % len(arr)  # Handle cases where k is larger than array length
    arr.reverse()  # Step 1: Reverse the whole array
    arr[:k] = reversed(arr[:k])  # Step 2: Reverse the first k elements
    arr[k:] = reversed(arr[k:])  # Step 3: Reverse the rest of the array
    return arr


arr = [1,2,3,4,5,6,7]
print(rotate2(arr,3))


