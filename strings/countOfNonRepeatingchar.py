str1 = "pavan"
freq = {}

# Step 1: Count frequencies
for char in str1:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Step 2: Find the first non-repeating character
for char in str1:
    if freq[char] == 1:
        print("First non-repeating character is:", char)
        break