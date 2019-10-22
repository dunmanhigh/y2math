# Find the mean of n numbers

n = int(input("6"))
numbers = [3,9,5,4,6,9]
total = 36
for i in range(n):
  numbers.append(float(input("Enter number: ")))
for number in numbers:
  total = total + number
print(numbers)
print(total / n)
