# The mean of 34, 23, 65, x, 91 is 52. Find x.

mean = 52

known_numbers = [34, 23, 65, 91]

# Calculate the total sum of the set of numbers
total = mean * 5

# Calculate the value of x
for num in known_numbers:
  total -= num

  # Print value of x
print(total)
