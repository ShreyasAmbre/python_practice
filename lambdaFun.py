from functools import reduce

print("Will learn of lambda function of python")

msg = lambda name: print("Hiii", name)

msg("Shreyas")

data = [2, 4, 3, 7, 6, 9]

# Called Function inside the function using lambda function
# filter() is an ibuilt function :- mainly use for true or false condition
evens = list(filter(lambda n: n % 2 == 0, data))
print(evens)

# map() inbuilt function: mainly used for do accept one value perform operation on it & give output
doubles = list(map(lambda n: n * 2, data))
print(doubles)


# reduce() inbuilt funtion :- mainly used to reduce the function
sum_all = reduce(lambda a, b: a + b, data)
print(sum_all)


# def sum_all(d):
#     res = 0
#     for i in d:
#         res = res + i
#     print(res)
#
# sum_all(data)
