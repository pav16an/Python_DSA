def intersection_array(arr1,arr2):
   r = []
   for i in arr1:
       for j in arr2:
           if i in arr2 and j not in arr1:
               r.append(i)
   print(r)
       


arr1 = [1,2,3,3,2,4,5,6,2]
arr2 = [1,2,7,5,3,2,6,2]
print(intersection_array(arr1,arr2))
            