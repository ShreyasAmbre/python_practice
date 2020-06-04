def div(a, b):
    print(a / b)


# above div() function is paramter
def smart_div(func):

    # below code is a new feature added to above normal div number is less then it get swap to denominator
    def inner(c, d):
        if c < d:
            c, d = d, c
        return func(c, d)

    return inner

div1 = smart_div(div)
div1(2, 4)