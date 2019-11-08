# Find x and y with these two equations:
# 3x + 4y = 24
# 4x + 3y = 22
import numpy as np 

equal1 = [3,4,24]
equal2 = [4,3,22]

np_equal1 = np.array(equal1)
np_equal2 = np.array(equal2)

np_equal3 = np_equal1 * 4
np_equal4 = np_equal1 * 3
np_equal5 = np_equal3 - np_equal4

print(np_equal5[2] / np_equal5[1])
