# Introduction to Computation and Programming Using Python
# Second Edition 
# John V. Guttag

# These are the finger exercises from every chapter
# None of the code is copied. This is how I solved the finger exercises
# Hopefully this can help some people in thier studies


# Chapter 2.2
'''
Write a program that.. 
    1. Examines 3 variables - x, y and z.
    2. Identifies the Odd numbers
    2. Prints the largest odd number
    3. if none are odd it should print something to that effect
'''
###########
# Code Below
###########

# import the needed random number generator library
import random

# Generate a random num between 0 and 99 and assign to variable
x = random.randint(0, 99)
y = random.randint(0, 99)
z = random.randint(0, 99)

# numlist is the 3 initial random numbers that we will iterate over
# to find the odd numbers
numlist = [x, y, z]

# oddlist is the empty list that we will be filling once we find the
# odd numbers
oddlist = []

# print the variables for visual clarity
print('x =',x, 'y =',y, 'z =',z)

# I created a function to return a bool if a number is even     
def iseven(numa):
    if numa%2 == 0:
        return True
    else:
        return False
# I created a function to retrun a bool if a numner is odd
def isodd(numa):
    if numa%2 > 0:
        return True
    else:
        return False

# For even num in initial list (numlist)
for nu in numlist:
    if isodd(nu): # if its odd
        list.append(oddlist, nu) # send to oddlist

if iseven(x) and iseven(y) and iseven(z): # if all is even
    print('sorry nothing odd') # say sorry 
else: # else
    print(max(oddlist)) # print the max (odd number) in the oddlist
