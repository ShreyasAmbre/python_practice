vowels = "aeiou"

input_String = "u"

for a in vowels:
    if input_String == a:
        print("Vowel")
        # break
else:
    # This statemet not get excecute because break keywprd is used
    # If break is not written after completing for loop it will also excecute else block
    print("Not Vowel")