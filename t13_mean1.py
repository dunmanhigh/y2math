# Find the mean of n numbers

n = int(input("Enter number of numbers: "))
numbers = []
total = 0
for i in range(n):
  numbers.append(float(input("Enter number: ")))
for number in numbers:
  total = total + number
print(numbers)
print(total / n)

# find the mean of 5, 10 and 15
numbers = [5, 10, 5]
total = numbers(0*1*2)
mean = total / 3
print(mean)
