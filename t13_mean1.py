# Find the mean of x numbers

x = int(input("Enter number of numbers: "))
numbers = []
total = 0
for i in range(x):
  numbers.append(float(input("Enter number: ")))
for number in numbers:
  total = total + number
print(numbers)
print(total / x)
