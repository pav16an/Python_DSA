def second_large(arr):
    s = sorted(arr)
    print(s[-2])
    
    
    
def second(arr):
     first,second = arr[0],arr[0]
    
     for num in arr:
         if num >  first:
             second = first
             first  = num
         elif num > second and num != first:
             second = num
     print(second)
                
arr = [1,2,3,4,56,6]
second(arr)