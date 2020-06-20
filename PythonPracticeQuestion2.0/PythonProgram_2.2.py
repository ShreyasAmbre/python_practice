# WAP to get a string from a given string where all occurrences of its second char have been
# changed to '$', except the first char itself.

s = "restart"
liststr = list(s)
i = 0
while i < len(s):
    c = s.count(s[i])
    if c == 2:
        chr = s.rindex(s[i])
        liststr[chr] = "$"
    i += 1
newStr = str(liststr)
print(newStr)