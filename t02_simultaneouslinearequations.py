# Find x and y with these two equations:
# 3x + 4y = 24
# 4x + 3y = 22
for x in range (-100,100):
  for y in range (-100,100):
    if ((3*x)+(4*y)) == 24 and ((4*x)+(3*y)) == 22:
      print(x,y)
      break
