# The mean of 49, 57, 89, x, 98 is 78. Find x.

mean = 78

known_numbers = [49, 57, 89, 98]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)
