# Find the mean of n numbers

n = int(input("Enter an integer number of numbers: ")) 

numbers = [float(input("Enter number: ")) for i in range(n)]

print(f"List of numbers: {numbers}\nMean of the numbers: {sum(numbers)/ n}") # print the list of numbers and the mean

