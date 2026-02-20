def missing_num(arr,n):
    sum_n = n * (n+1) //2
    curr_n = sum(arr)
    missing_val = sum_n - curr_n
    print(missing_val)
    
arr = [1,2,3,5,6]
n = 6 
missing_num(arr,n)
    
