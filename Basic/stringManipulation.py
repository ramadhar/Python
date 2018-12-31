myString = "abcdefgh"

print(myString)

# extract element from a strings

print("first charactor of myString is: ", myString[0])
print("4th charactor of myString is: ", myString[3])
print("Last charactor of myString is: ", myString[-1])
print("Last charactor of myString is: ", myString[7])

# get length of string
print(len(myString))

# string slicing
print(myString[2:])

# print index 2 to index 4
print(myString[2:5])

# print 2 to last-1 elements
print(myString[1:-1])

# slicing with interval
print(myString[0:-1:2])

# print all element
print(myString[::])

# reverse of a string
print(myString[::-1])

newString = myString[::-1]
print(newString)

# string concatenation
str1 = "Ram"
str2 = " ia a good boy"

print(str1 + str2)
print(str1 * 5)

str3 = str1 + str2
print(str3.upper())

# get a list from string
print(str3.split())

# split with a delimiter
print(str3.split('a'))





