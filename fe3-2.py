## Let s be a string that contains a sequence of decimal numbers
## separated by commas, eg s = '1.23,2.4,3.123'.
## Write a program that prints the sum of the numbers in s.
s = '1.23,2.4,3.123,9.234,2.3434234'

def iter(string1): 
    l = [] # empty list to store the found string floats
    m = '' # empty string to store the temporary numbers and decimals using the 'm += 1' 
    count = 0 # counter used only for the last decimal

    for i in string1:
        if i != ',':
            m += i
            count += 1
        elif i == ',':
            l.append(m)
            m = ''
            count += 1
            continue
        if count == len(string1):
            l.append(m)
            break
    return l

l = iter(s)
total = 0

for i in l:
    fl = float(i)
    total += fl

print(total)
