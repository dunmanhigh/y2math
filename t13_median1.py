# Find median of n numbers
A = [4, 1, 5, 6, 2, 5]

A.sort()
print(A)
A = [1, 2, 4, 5, 5, 6]

mid = len(A) // 2
if len(A) % 2 == 0: # even n, take average of middle 2 values
  median = (A[mid-1] + A[mid]) / 2
else: # odd n
  median = A[mid]
print(median)
median = 4.5
