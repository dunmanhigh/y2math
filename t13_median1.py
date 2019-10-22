# To find the median of n numbers
A = [65, 34, 51, 62, 27, 75]

A.sort()
print(A)

mid = len(A) // 2
if len(A) % 2 == 0: #If n is even
  median = (A[mid-1] + A[mid]) / 2
else: #If n is odd
  median = A[mid]
print(median)
