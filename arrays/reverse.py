def reverse_Arr(arr):
  arr1 = []
  for i in range(len(arr)-1,-1,-1):
    arr1.append(arr[i])
  return arr1


def reverse_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_arr(arr))
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_Arr(arr))
