# The mean of 34, 23, 65, x, 91 is 52. Find x.

mean = 52

known_numbers = [34, 23, 65, 91]

total = mean * 5

for num in known_numbers:
  total -= num

print(total)

mean = 52
known = [34, 23, 65, 91]
sumOfNumbers = mean * 5
for number in known:
  sumOfNumbers -= number
print(str(sumOfNumbers) + " is the value of x")
