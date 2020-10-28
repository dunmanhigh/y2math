# The mean of 34, 23, 65, x, 91 is 58. Find x.

mean = 58

known_numbers = [34, 23, 65, 91]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)
