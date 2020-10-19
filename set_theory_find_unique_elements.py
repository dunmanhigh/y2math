# Find the unique elements in arr

arr = [1, 3, 9, 0, 2, 5, 18, 3, 9, 2]

appeared = {}

for i in range (len(arr)):
    if arr[i] in appeared:
        appeared[arr[i]] += 1
    else:
        appeared[arr[i]] = 1

for i in appeared:
    if appeared[i] == 1:
        print(i, end=" ")