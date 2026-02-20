n = input("enter a string: ")
n = n.lower()
vow = 0
con = 0
vowels = ["a","e","i","o","u"]
for i in range(len(n)):
  if n[i] in vowels:
    vow+=1
  else:
    con+=1
print("number of vowels :",vow)
print("number of consonants:",con)