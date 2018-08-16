
# ================
# 15_Ranges.py
# ================

# RANGES

# ranges, list of ranges, index, slicing, reverse order

# In python 3, range is a built in type
# in python 2, range is a function.

# We can create a range by specifying an end value.
# This gives result "range(0, 100)" showing you how to make a
# range object with a start of 0

print(range(100))

print("="*20)

# we get best value by using ranges to iterate over values
# We can also use ranges to create other objects like lists.

# This command creates a list with values from 0 to 10 (not inclusive) and then prints them

myList = list(range(10))
print(myList)

print("="*20)

# we can specify start and interval

even = list(range(0, 10, 2)) # even because it starts from 0 with interval 2
odd = list(range(1, 10, 2)) # odd because it starts from odd (1) with interval 2
print(even)
print(odd)

print("="*20)


# python 3 is very efficient in terms of memory
# so both these ranges will use the same amount of memory

range(0, 10)
range(0, 100000000)

print("="*20)

# however if you create lists of large ranges, the list themselves will occupy big memory


even = list(range(0, 1000, 2))
odd = list(range(1, 1000, 2))
print(even)
print(odd)

print("="*20)


# Note that in python 2, ranges were calculated and returned as sequences
# Python 2 also had function called xrange(). This is the same as range.

# Ranges don't support all the operations that you can perform on sequences.
# This is because ranges represent sequences that follow a defined pattern.
# For example, the multiplication & concatenation operators to repeat a range are not allowed.
# Other than that, you can perform all the usual sequence operations of ranges.

# How to access individual members of a range using index

myString = "abcdefghijklmnopqrstuvwxyz"
print(myString.index('e'))  # Gives 4. meaning character e is in position 4 (starting from 0)
print(myString[4])  # Gives e. meaning that character in position 4 is e.

print("="*20)

# We can also apply index function to ranges

smallDecimals = range(0, 10)
print(smallDecimals)
print(smallDecimals.index(3)) # prints 3 meaning 3 is in position 3

print("="*20)


# you can also index into a range.
# in this case, we get value 51, which is the odd number in position 25

odd = range(1, 100, 2)
print(odd)
print(odd[25])

print("="*20)

# You can check if the value you pass is in a range using "in" operator
# in this case we want to check if number entered is divisible by seven

sevens = range(7, 100, 7)
x = int(input("Please enter a number less than 100: "))
if x in sevens:
    print("Number {} is divisible by 7".format(x))
else:
    print("Number {} is Not divisible by 7".format(x))

print("="*20)


# Slice Ranges


smallDecimals = range(0, 10)
print(smallDecimals)
print(smallDecimals.index(0))
print(smallDecimals.index(1))
print(smallDecimals.index(2))
print(smallDecimals.index(3))
print(smallDecimals.index(4))
print(smallDecimals.index(5))
print(smallDecimals.index(6))
print(smallDecimals.index(7))
print(smallDecimals.index(8))
print(smallDecimals.index(9))


print()
myRange = smallDecimals[::2] # if you don't specify start and end, it takes originals 0, 10
print(myRange)
print(myRange.index(0)) # 0 is in position 0
print(myRange.index(2)) # 1 is in position 2
print(myRange.index(4)) # 2 is in position 4
print(myRange.index(6)) # 3 is in position 6
print(myRange.index(8)) # 4 is in position 8

print("="*20)


# Here is another example to show range slices


decimals = range(0, 100) # original range 0 to 100
print(decimals)

myIndex = decimals[3:40:3] # Index of decimals starting at 3, to 40 interval 3
print(myIndex)

for i in myIndex: # Prints everything in myIndex from 3 to 39  interval 3
    print(i)

print("==========")

for i in range(3, 40, 3): # New range similar to myIndex
    print(i)


print(myIndex == range(3, 40, 3)) # comes true because they are the same

print("="*20)

# ==================
# Range comparisons:
# ==================

# Example 1
# The third line comparison shows true because the comparison is on the results of both
# The results are the same.

decimals = range(0, 100) # Range from 0 to 100
myRange = decimals[3:40:3] # slice it with index starting 3, to 40 intervals 3
print(myRange == range(3, 40, 3)) # index myRange is equal to range(3, 40, 3) i.e. same result

print("="*20)

# Here is how we can check the results of above
# We see here that second and third line have same results, hence equal

print(list(decimals))  # Prints range 0 to 99 with default interval of 1
print(list(myRange)) # prints range 0 to 39 with interval of 3
print(list(range(3, 40, 3))) # prints range 0 to 39 with interval of 3
print()

print("="*20)


# Range comparisons
# Example 2
# These two are the ranges we are comparing

print(range(0, 5, 2))
print(range(0, 6, 2))
print()

# This command prints true because the results of these ranges are same

print(range(0, 5, 2) == range(0, 6, 2))

print("="*20)

# Here is how to check the results of the ranges using list.
# We see the results give the same value, hence the results above showing that they are equal

print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

print("="*20)

# Slicing using negative numbers
# Here we print the numbers in reverse

myRange = range(0, 20)
print(myRange) # This prints our range command
print()

# Now we are going to use for loop to print the numbers in the index
# starts from end, to beginning, with interval of -2, meaning we are starting from end/reverse
# We can see this prints from 19 to 1 using interval of 2

for i in myRange[::-2]:
    print(i)

print()

# prints from 19 towards 1 using interval or 1

for i in myRange[::-1]:
    print(i)

print("="*20)

# you can specify start point and interval
# Since this is reverse, we start from 17, to 2 with interval of 2

for i in myRange[17:2:-2]:
    print(i)

print("="*20)

# Here we are using the normal way and starting from 0, to end, with interval of 2

for i in myRange[::2]:
    print(i)

print("="*20)


# You can also specify start and end points for the forward loop
# This one starts from 3, with interval of 2 and ends at 15

for i in myRange[3:15:2]:
    print(i)

print("="*20)

# You can also print myRange in list form.
# Both forward and reverse

print(myRange)
print(list(myRange[::2]))
print(list(myRange[3:15:2]))
print(list(myRange[::-2]))
print(list(myRange[17:2:-2]))

print("="*20)

# How to process range in reverse order for strings

forwardString = "Python is a very powerful language"
print(forwardString) # Types same way it is
print(forwardString[::-1]) # Reverses it from end to start using interval of 1
print()

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString) # Types backstring same way it is
print(backString[::-1]) # Reverses it from end to start using interval of 1
print()

print("="*20)

# How to print range in reverse using for loop

r = range(0, 10)
for i in r[::-1]:
    print(i)

print("="*20)

# Example 3 for ranges

firstRange = range(0, 100, 4)
print(firstRange) # This is the firstRange
print(list(firstRange)) # These are the results of firstRange

print("="*20)

# In secondRange, the result is 20, which is the interval 5 multiplied by first interval 4

secondRange = firstRange[::5]
print(secondRange) # This is the secondRange. looks like result show 5 x 4 = 20
print(list(secondRange)) # Results show interval of 20
print()
# you can also check results using a for loop

for i in secondRange:
    print(i)

