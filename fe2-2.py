# examine xyz and print the largets odd number among them
# if none are odd, print it

import random

x = random.randint(0,99)
y = random.randint(0,99)
z = random.randint(0,99)

numlist = [x, y, z]
oddlist = []

for i in numlist:
    print(i)
    if i%2 != 0:
        oddlist.append(i)

print('oddlist=', oddlist)

if oddlist.__len__() > 0:
    print('max odd=', max(oddlist))
else:
    print('nothing to see here')