# Find the cube root of a perfect cube
x = int(input('Enter an Int '))

ans = 0 
while ans**3 < abs(x):
    print('vlaue of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)
    ans += 1
    #ans -= 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('the cube root of', x, 'is', ans)