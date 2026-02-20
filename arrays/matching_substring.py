def match_sub(s):
    res = []
    for i in range(len(s)):
        for j in range(len(s)):
           if i != j and s[i]  in s[j] and s[i] not in res:
              res.append(s[i])
    print(res)
            
           
s = ["hello","el" ,"self","selfemployement", "pavan"]
match_sub(s)