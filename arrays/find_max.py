def find_max(arr):
  for i in range(len(arr)):
    max = arr[0]
    if arr[i] > max:
      max = arr[i]
  return max

def max_of_array(arr):
  return max(arr)

arr = [1, 2, 3, 99, 5, 6, 104]
print(find_max(arr))
arr = [1, 2, 3, 99, 5, 6, 104]
print(max_of_array(arr))