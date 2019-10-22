# The mean of 75, 60, 98, x, 94 is 52. Find x.

mean = 52

known_numbers = [75, 60, 98, 94]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)
