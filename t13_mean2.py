# The mean of 34, 23, 65, x, 91, 48 is 53. Find x.

mean = 53

known_numbers = [34, 23, 65, 91, 48]

total = mean * 6

for num in known_numbers:
  total -= num
print(total)

