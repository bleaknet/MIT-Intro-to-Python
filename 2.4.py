#Section 2.4  finger exercise

import random

oddlist = []
numlist = []
x = 1

while (x != 11):
    r = random.randint(0, 99)
    list.append(numlist, r)
    x += 1

for num in numlist:
    if num%2 > 0:
        list.append(oddlist, num)

if len(oddlist) == 0:
    print('sorry nothing odd here')
else:
    print('numlist =', numlist)
    print('oddlist =', oddlist)
    print('max odd num', max(oddlist))
