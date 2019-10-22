# The mean of 27, 34, 23, 65, y, 91 is 54. Find y.

mean = 54

known_numbers = [27, 34, 23, 65, 91]

total = mean * 6

for num in known_numbers:
  total -= num

print(total)
