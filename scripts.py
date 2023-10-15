## Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")
    


## Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


if((n%2 != 0)): 
    print( "Weird")
elif((n%2 == 0) & (6<=n<=20) ):
    print( "Weird")
else:
    print("Not Weird")

## Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print( a+b)
print(a-b)
print(a*b)

## Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

## Loops

if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i**2)

## Write a function

def is_leap(year):
    leap = False
    
    if year%100 == 0 and ((year//100)%4) == 0:
        leap = True
    elif year%100 == 0 and ((year//100)%4) != 0:
        leap = False
    elif year%4 == 0:
        leap = True
    else:
        leap = False
    
    return leap

## Print Function

if __name__ == '__main__':
    n = int(input())
    
num = ""
x=1
for i in range(n):
    num = num + str(x)
    x +=1
print(num)  

## List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
permutation = list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n)

print(permutation)
        
## sWAP cASE

def swap_case(s):
    swaped = ""
    for x in s:
        if x.isupper() == True:
            swaped+=(x.lower())
        else:
            swaped+=(x.upper())
    return swaped

## String Split and Join

def split_and_join(line):
    new_line = line.split(" ")
    new_line = "-".join(new_line)
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

## What's Your Name?

def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

## Mutations

def mutate_string(string, position, character):
    
    return(string[:position] + character + string[position + 1:])

## Find a string

def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        position = string.find(sub_string)
        string = string[position+1:]
        count +=1
    return count

## String Validators 

if __name__ == '__main__':
    s = input()

out = False 
for x in s:
    if x.isalnum():
        out = True
print(out)

out = False 
for x in s:
    if x.isalpha():
        out = True
        break
print(out)

out = False 
for x in s:
    if x.isdigit():
        out = True
        break
print(out)

out = False 
for x in s:
    if x.islower():
        out = True
        break
print(out)

out = False 
for x in s:
    if x.isupper():
        out = True
        break
print(out)

## Text Wrap

import textwrap

def wrap(string, max_width):
    for x in range(len(string)):
        new = string[0:max_width]
        print(new)
        string = string[max_width:]
        if(len(string) <= max_width):
            return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

##  Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

if arr[0] < arr[1]:
    first = arr[1]
    second = arr[0]
elif arr[1] < arr[0]:
    first = arr[0]
    second = arr[1]
elif arr[1] == arr[0]:
    first = arr[0]
    second = arr[1]
    
for j in range (2, n):
    if((arr[j] > second) | (first == second)):
        if(arr[j]>first):
            second = first
            first = arr[j] 
        elif(arr[j] < first):
            second = arr[j]

print(second)

## Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
marks = list(student_marks[query_name])
avarage = (sum(marks)/len(marks))

print('%.2f'% avarage)

## Lists

if __name__ == '__main__':
    N = int(input())
    
lista = []

for j in range(N):
    instruction = input().split()
    if instruction[0] == "insert":
        lista.insert(int(instruction[1]), int(instruction[2]))
    elif instruction[0] == "print":
        print(lista)
    elif instruction[0] == "remove":
        lista.remove(int(instruction[1]))
    elif instruction[0] == "append":
        lista.append(int(instruction[1]))
    elif instruction[0] == "sort":
        lista.sort()
    elif instruction[0] == "pop":
        lista.pop()
    elif instruction[0] == "reverse":
        lista.reverse()

## Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

t = tuple(integer_list)
print(hash(t))

##  String Formatting


def print_formatted(number):
    final = len(bin(number)[2:]) #I found this online to print the exact output
    for j in range(1, number+1):
        decimal = str(j)
        octal = oct(j)[2:]
        hexadec = hex(j)[2:].upper()
        binary = bin(j)[2:]
        print(decimal.rjust(final),octal.rjust(final),hexadec.rjust(final),binary.rjust(final))

## Capitalize!

# Complete the solve function below.
def solve(s):
    nom = s.split(' ')
    firstup = [j.capitalize() for j in nom]
    return(" ".join(firstup))

## Introduction to Sets

# def average(array):
    set_num = set(array)
    return(sum(set_num)/len(set_num))


## Symmetric Difference


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n1 = int(input())
    set1 = set(map(int, input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))

one = set1.difference(set2)
two = set2.difference(set1)

uni = one.union(two)
for j in sorted(uni):
    print(j)


## No Idea!


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))

happiness = 0
for j in arr:
    if j in A:
        happiness += 1
    elif j in B:
        happiness -= 1
        
print(happiness)

## Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

tot_count = set()
for j in range(n):
    tot_count.add(input())
print(len(tot_count))


## Set .discard(), .remove() & .pop()

n = int(input())
set1 = set(map(int, input().split()))
N = int(input())

for j in range(N):
    instruction = list(map(str, input().split()))
    if instruction[0] == "pop":
        set1.pop()
    elif instruction[0] == "remove":
        if int(instruction[1]) in set1:
            set1.remove(int(instruction[1]))
    elif instruction[0] == "discard":
        set1.discard(int(instruction[1]))
    
print(sum(set1))

## Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
sn = set(map(int, input().split()))
b = int(input())
sb = set(map(int, input().split()))

sa = sn.union(sb)

print(len(sa))

##  Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
sn = set(map(int, input().split()))
b = int(input())
sb = set(map(int, input().split()))

sa = sn.intersection(sb)
print(len(sa))

## Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
sn = set(map(int, input().split()))
b = int(input())
sb = set(map(int, input().split()))

sa = sn.symmetric_difference(sb)
print(len(sa))

## Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
sn = set(map(int, input().split()))
b = int(input())
sb = set(map(int, input().split()))

sa = sn.difference(sb)
print(len(sa))

## Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
S = set(map(int, input().split()))
b = int(input())

for j in range(b):
    instruction = list(map(str, input().split()))
    new = set(map(int, input().split()))
    if instruction[0] == "intersection_update":
        S.intersection_update(new)
    elif instruction[0] == "update":
        S.update(new)
    elif instruction[0] == "symmetric_difference_update":
        S.symmetric_difference_update(new)
    elif instruction[0] == "difference_update":
        S.difference_update(new)

print(sum(S))

## Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for j in range(t):
    a = int(input())
    sa = set(map(int, input().split()))
    b = int(input())
    sb = set(map(int, input().split()))
    if sa.issubset(sb):
        print("True")
    else:
        print("False")

## collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())

money = 0


for j in range(n):
    shoe, amount = map(int, input().split())
    if sizes[shoe] != 0:
        sizes[shoe] -= 1
        money += amount
        

print(money)

## Calendar Module


# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

m , d, y = list(map(int,input().split()))

cal = calendar.weekday(y, m, d)

print(calendar.day_name[cal].upper())

## Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, X = input().split()

marks = list()

for j in range(int(X)):
    av = map(float, input().split())
    marks.append(av)
    
student = zip(*marks)
for m in student:
    print(sum(m)/len(m))


## Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    new = numpy.array(arr[::-1], float)
    return(new)


## Shape and Reshape

import numpy

arr = input().strip().split(' ')
new = numpy.array(arr, int)
new.shape = (3,3)
print(new)

## Transpose and Flatten

import numpy

N, M = input().split()

arr_joined = []
for j in range(int(N)):
    arr = list(map(int,input().split()))
    arr_joined.append(arr)
new = numpy.array(arr_joined)

print(numpy.transpose(new))
print(new.flatten())


#############
# PROBLEM 2 #
#############


## Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    anterior = candles[0]
    amount = 1
    for x in range(len(candles)-1):
        r = candles[x+1]
        if r > anterior:
            anterior = r
            amount = 1
        elif r == anterior:
            amount += 1
    return(amount)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


## Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    for x in range(v1*x2):
        if x1 == x2:
            return("YES")
            break
        elif (x1 < x2) & (v1 <= v2):
            return("NO")
            break
        elif (x1 > x2) & (v1 >= v2):
            return("NO")
            break
        else:
            x1 += v1
            x2 += v2
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


## Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    suma = 0
    start = 5
    for x in range(n):
        likes = start//2
        suma += likes
        start = likes * 3
    return(suma)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

## Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num = arr[-1]
    stat = 0
    for x in range(len(arr)-2, -1, -1):
        if num < arr[x]:
            arr[x +1] = arr[x]
            print(" ".join(map(str, arr)))
        else:
            arr[x + 1] = num
            print(" ".join(map(str, arr)))
            stat = 1
            break
    if stat == 0:
        arr[0] = num
        print(" ".join(map(str, arr)))
                
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

## Insertion Sort - Part 2


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(m, arr):
    num = arr[m]
    stat = 0
    for x in range(m-1, -1, -1):
        if num < arr[x]:
            arr[x +1] = arr[x]
        else:
            arr[x + 1] = num
            stat = 1
            break
    if stat == 0:
        arr[0] = num

def insertionSort2(n, arr):
    for j in range(1, len(arr)):
        insertionSort1(j, arr)
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

## Recursive Digit Sum


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def super_aux(digit):
    aux = map(int, list(digit))
    d = str(sum(aux))
    while len(d) != 1:
        aux = map(int, list(d))
        d = str(sum(aux))
    return(int(d))
        
    
def superDigit(n, k):
    dig = map(int, list(n))
    d = str(sum(dig) * k)
    return super_aux(d)
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()