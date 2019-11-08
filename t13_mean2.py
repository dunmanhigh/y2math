# The mean of 34, 23, 65, x, 91 is 52. Find x.

mean = 52

known_numbers = [34, 23, 65, 91]

total = mean * 5
      = 52 * 5
      = 260
for num in known_numbers:
  total -= num
         = 34 + 23 + 65 + 91
         = 213
       x = 260 - 213
         = 47
print(total)
