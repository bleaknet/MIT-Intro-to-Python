# write a program that asks the user to enter an int
# and prints 2 ints, root and pwr
# such that 1 < pwr < 6 and root**pwr == int
# if no int exists then print that

# root**pwr == x

pwr = 2
root = 0
x = input('please input an int')

for i in range(2,6):
    #print('i=', i)
    rooter = 0
    while rooter**i < x:
        #print(root)
        rooter += 1
        if rooter**i == x:
            print(rooter,'**', i, '=',x)
            root = rooter
            pwr = i
            break
#root = rooter
if root**pwr != x:
    print('nothing')
print(root**pwr)
#print('root=',root)
print('pwr=', pwr)
#print("x=", x)

        
    