# WAP to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.

str = "Py"
strlen = len(str)

def newString(str):
    str1 = str[0:2]
    str2 = str[-2:]
    newStr = str1 + str2
    print(newStr)


if strlen < 3:
    print(str)
else:
    newString(str)
