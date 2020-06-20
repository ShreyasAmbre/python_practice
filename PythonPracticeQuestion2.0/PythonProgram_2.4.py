# WAP to find the first appearance of the substring 'not' & 'poor' from a given string, if 'not'
# follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

statement = "Hotel is not poor to have dinner"

val = statement.replace("not poor", "good")
print(val)
