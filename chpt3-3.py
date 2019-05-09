''''
x = 25 
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step 
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('failed on square root of', x)
else:
    print(ans, 'is lose to square root of', x)
'''
import random

#x = random.randint(0,999) 
x = -25
epsilon = 0.01
numGuesses = 0 
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0


while abs(ans**2 - x) >= epsilon:
    print(abs(ans**2 - x))
    print('low=', low, 'high=', high, 'ans=', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    print(abs(ans**2 - x))
    
print('numGuesses=', numGuesses)
print(ans,'is close to square root of', x)
