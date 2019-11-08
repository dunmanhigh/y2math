#finding cube root of 8
cube=8
for guess in range(abs(cube)+1):
    if guess**3>=abs(cube):
        break
if guess**3!=cube:
        print(cube, 'is not a perfect cube')
else:
    if cube<0:
        guess=-guess
    print('the cube root of ', str(cube), ' is ', str(guess))
