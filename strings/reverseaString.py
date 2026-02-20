#reverse a string
str = "pavan"
l = []
for i in range(len(str)-1,-1,-1):
  l.append(str[i])

print(l)


rev = str[::-1]
print(rev)