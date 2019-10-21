# The mean of 34, 23, 65, x, 90 is 52. Find x.

mean = 52

known_numbers = [34, 23, 65, 91]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)
