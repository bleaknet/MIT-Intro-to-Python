# ask the user to input 10 ints.
# prints the larget odd number that was entered
# if no odd number was enetered it should print that to that effect

import random
numList = []
oddList = []

for i in range(10):
    numList.append(random.randint(0,99))

print(numList)

for i in numList:
    if i%2 != 0:
        oddList.append(i)

print(max(oddList))