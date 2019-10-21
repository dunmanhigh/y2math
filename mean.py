# The mean of 1, 2, 7, x, 11 is 7. Find x.

mean = 7

known_numbers = [1, 2, 7, 11]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)
